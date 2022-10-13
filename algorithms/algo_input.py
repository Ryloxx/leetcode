from collections import deque
from itertools import chain
from operator import itemgetter
from func_timeout import FunctionTimedOut, func_timeout
from pathos.multiprocessing import ProcessingPool as Pool
import os
import sys
from sys import setrecursionlimit
import textwrap
from timeit import default_timer
from traceback import format_tb
from typing import Any, Callable, Generator, List, Optional, Tuple

IS_DEBUG = "DEBUG" in os.environ \
        and os.environ["DEBUG"].lower() == "true"
CI = "CI" in os.environ \
    and os.environ["CI"] == "true"

LEETCODE_MAX_RECURSION_DEPTH = 20_000
LEETCODE_MAX_MEMORY = 800 * 1024 * 1024  # 800 MB
LEETCODE_MAX_TIMEOUT_MS = 1000 * 60 * 60 if IS_DEBUG else 3000  # 3000 ms
BATCH_SIZE = 5
MAX_PRINT_WIDTH_RESULT = sys.maxsize if IS_DEBUG else 200


def disableStd():
    null = open(os.devnull)
    temp = sys.stderr, sys.stdout
    if not IS_DEBUG:
        sys.stderr = null
        sys.stdout = null

    def enableStd():
        sys.stderr, sys.stdout = temp

    return enableStd


def limitMemory(memoryLimit: int):
    if sys.platform != "win32":
        import resource
        resource.setrlimit(resource.RLIMIT_AS,
                           (memoryLimit, resource.RLIM_INFINITY))
    else:
        import win32api
        import win32job
        job = win32job.CreateJobObject(None, 'LeetCode Env')  # type: ignore
        currentProcess = win32api.GetCurrentProcess()
        jobInfo = win32job.QueryInformationJobObject(
            job, win32job.JobObjectExtendedLimitInformation)  # type: ignore
        jobInfo["ProcessMemoryLimit"] = memoryLimit
        jobInfo["BasicLimitInformation"]["LimitFlags"] |=\
            win32job.JOB_OBJECT_LIMIT_PROCESS_MEMORY
        win32job.SetInformationJobObject(
            job,  # type: ignore
            win32job.JobObjectExtendedLimitInformation,
            jobInfo)
        win32job.AssignProcessToJobObject(job, currentProcess)  # type: ignore


def getLastError():
    type, value, trace = sys.exc_info()
    return type, value, ''.join(format_tb(trace))


def parseResult(res):
    try:
        res.__next__
        res = list(res)
    except AttributeError:
        pass
    if isinstance(res, list):
        res = list(map(parseResult, res))
    return res


def sub_f(args):
    fnc, *args = args
    limitMemory(LEETCODE_MAX_MEMORY)
    setrecursionlimit(LEETCODE_MAX_RECURSION_DEPTH)
    try:
        start = default_timer()
        res = func_timeout(LEETCODE_MAX_TIMEOUT_MS / 800, fnc, args)
        end = default_timer()
        return ((parseResult(res), end - start), None)
    except FunctionTimedOut as x:
        return ((None, -1), (type(x), x, ''))
    except Exception:
        error = getLastError()
        return ((None, -1), error)


def run_in_sub(fnc: Callable, args: List[List[Any]]):
    pool = Pool(1 if IS_DEBUG else None)
    pool.restart()
    ret_list = pool.map(sub_f, [(fnc, *x) for x in args])
    pool.close()
    return ret_list


def in_env(fnc: Callable, args):

    results = []
    for _ in [
            args[idx:idx + BATCH_SIZE]
            for idx in range(0, len(args), BATCH_SIZE)
    ]:
        results.extend(run_in_sub(fnc, _))

    def parse(run_result):
        executionInfo = {
            "Time": "-",
            "Execution Error": None,
            "Result": None,
            "Expected": None
        }
        (res, runtime), error = run_result
        if error:
            if error[0] == FunctionTimedOut:
                executionInfo["Execution Error"] = "Time Limit Exceeded"
            elif error[0] == MemoryError:
                executionInfo["Execution Error"] = "Memory Limit Exceeded"
            else:
                executionInfo["Execution Error"] = error[1]
        if runtime and runtime * 1000 > LEETCODE_MAX_TIMEOUT_MS:
            executionInfo["Execution Error"] = "Time Limit Exceeded"
        executionInfo["Time"] = "%.2f ms" % (runtime *
                                             1000) if runtime >= 0 else "N/A"
        executionInfo["Result"] = res
        return executionInfo

    return list(map(parse, results))


def wrapp_class(Class_type: Callable):

    def process(class_args: List[Any], steps: List[Tuple[str, List[Any]]]):
        obj = Class_type(*class_args)
        return list(map(lambda step: getattr(obj, step[0])(*step[1]), steps))

    return process


def truncate(obj: Any, width: int):
    return textwrap.shorten(str(obj), width=width, placeholder="...")


def run(fnc: Callable,
        testCases: List[Tuple[List[Any], Any]],
        comparator: Callable[[Any, Any], bool] = lambda x, y: x == y):
    execution_infos = in_env(fnc, list(map(itemgetter(0), testCases)))
    for no, (execution_info, expected) in enumerate(
            zip(execution_infos, map(itemgetter(1), testCases))):
        execution_info["Expected"] = expected
        success = comparator(
            execution_info["Result"],
            expected) and execution_info["Execution Error"] is None
        result = "\u001B[32mPass\u001B[0m" if success\
            else "\u001B[31mFail\u001B[0m"
        execution_info["Expected"] = truncate(str(execution_info["Expected"]),
                                              MAX_PRINT_WIDTH_RESULT)
        execution_info["Result"] = truncate(
            str(execution_info["Result"]),
            MAX_PRINT_WIDTH_RESULT,
        )
        print(f"Test nº \u001B[34m{no}\u001B[0m"
              f" - {result}"
              f" - {execution_info}")
        if CI and not success:
            print('Exiting on fail because CI detected', file=sys.stderr)
            exit(1)
    else:
        print("Done")


""" HELPERS """


def any_order(a, b):
    return a is not None and b is not None and sorted(a) == sorted(b)


def _formated_tree(tree: List[List[Any]], emptyChar: str):
    max_value_length = max(
        3, len(max((max(map(str, level), key=len) for level in tree),
                   key=len)))
    max_value_length = max_value_length + (max_value_length + 1) % 2
    total_width = len(tree[-1]) * max_value_length
    return '\n'.join("".join(
        map(
            lambda value: str(value if value is not None else emptyChar).
            center(max_value_length).center(total_width >> level),
            tree[level])) for level in range(len(tree)))


class TreeNode:

    @staticmethod
    def create_tree(nums: List[Optional[int]]):
        if not nums:
            return None
        root = TreeNode(nums[0])
        current = [root]
        i = 1
        while i < len(nums) and current:
            temp = []
            for j in current:
                if j:
                    left = TreeNode(
                        nums[i]
                    ) if i < len(nums) and nums[i] is not None else None
                    i += 1
                    right = TreeNode(
                        nums[i]
                    ) if i < len(nums) and nums[i] is not None else None
                    i += 1
                    j.left, j.right = left, right
                    temp += [left, right]
            current = temp
        return root

    @staticmethod
    def _tree(root: "TreeNode", emptyChar="x"):
        current: List[Optional[TreeNode]] = [root]
        tree = []
        while current.count(None) != len(current):
            tree.append(current)
            current = list(
                chain.from_iterable([i.left, i.right] if i else [None, None]
                                    for i in current))
        return _formated_tree([
            list(map(lambda x: x.val if x else None, level)) for level in tree
        ], emptyChar)

    @staticmethod
    def are_equal(tree_1, tree_2: Optional["TreeNode"]) -> bool:

        def nodes(
            root: Optional["TreeNode"]
        ) -> Generator[Optional[Any], None, Optional[List[Optional[int]]]]:
            if not root:
                return []
            traversal: List[Optional[TreeNode]] = [root]
            left = empty_count = 0
            while left + empty_count < len(traversal):
                empty_count = 0
                for idx in range(left, len(traversal)):
                    node = traversal[idx]
                    if not node:
                        traversal.append(None)
                        traversal.append(None)
                        empty_count += 2
                    else:
                        traversal.append(node.left)
                        traversal.append(node.right)
                    yield node.val if node else None
                    left += 1

        return list(nodes(tree_1)) == list(nodes(tree_2))

    @staticmethod
    def in_order(tree_1: Optional["TreeNode"]):
        if not tree_1:
            return
        yield from TreeNode.in_order(tree_1.left)
        yield tree_1.val
        yield from TreeNode.in_order(tree_1.right)

    @staticmethod
    def is_valid_binary_tree(tree_1: "TreeNode"):

        def dfs(node, m, M):
            if not node:
                return True
            if not m < node.val < M:
                return False
            return dfs(node.left, m, node.val) and dfs(node.right, node.val, M)

        return dfs(tree_1, -float('inf'), float('inf'))

    @staticmethod
    def get_height(tree_1: Optional["TreeNode"],
                   minHeight: int | bool = False):
        if not tree_1:
            return 0
        minHeight = int(bool(minHeight))
        return 1 + (max, min)[minHeight](
            TreeNode.get_height(tree_1.left, minHeight),
            TreeNode.get_height(tree_1.right, minHeight))

    @staticmethod
    def get_height_diff(tree_1: "TreeNode"):
        return TreeNode.get_height(tree_1) - TreeNode.get_height(tree_1, True)

    def __init__(self,
                 val: Any = 0,
                 left: Optional["TreeNode"] = None,
                 right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return TreeNode._tree(self)


class NTreeNode:

    def __init__(self,
                 val: Optional[Any] = None,
                 children: Optional[List["NTreeNode"]] = None):
        self.val = val
        self.children = children

    def append_child(self, node: Optional["NTreeNode"]):
        if self.children is None:
            self.children = [node]
        elif node:
            self.children.append(node)

    @staticmethod
    def create_tree(nums: List[Optional[int]]):
        root = None
        parents = deque()
        current_parent = None
        for value in nums:
            if value is None:
                current_parent = parents.popleft()
                continue
            node = NTreeNode(value)
            parents.append(node)
            if current_parent:
                current_parent.append_child(node)
            else:
                root = node

        return root


class ListNode:

    @staticmethod
    def create_list(nums: List[Optional[int]]):
        root = ListNode()
        current = root
        for i in nums:
            current.next = current = ListNode(i)
        return root.next

    @staticmethod
    def get(list_head: Optional["ListNode"], idx: int):
        if not list_head:
            raise TypeError
        if idx < 0:
            raise IndexError
        head: "ListNode" = list_head
        while idx:
            if not head.next:
                raise IndexError
            head = head.next
            idx -= 1
        return head

    @staticmethod
    def are_equal(list_1: Optional["ListNode"],
                  list_2: Optional["ListNode"]) -> bool:
        while (list_1 is not None and list_2 is not None
               and list_1.val == list_2.val):
            list_1 = list_1.next
            list_2 = list_2.next
        return list_1 is None and list_2 is None

    def __init__(self,
                 val: Optional[Any] = 0,
                 next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        res = []
        i = self
        while i:
            res.append(i.val)
            i = i.next
        return str(res)
