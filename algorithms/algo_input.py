from itertools import chain
from multiprocessing import Process, Queue
import os
from queue import Empty
import sys
from sys import setrecursionlimit
import textwrap
from timeit import default_timer
from traceback import format_tb
from typing import Any, Callable, List, Optional, Tuple

IS_DEBUG = "DEBUG" in os.environ \
        and os.environ["DEBUG"].lower() == "true"

LEETCODE_MAX_RECURSION_DEPTH = 20_000
LEETCODE_MAX_MEMORY = 100 * 1024 * 1024  # 100 MB
LEETCODE_MAX_TIMEOUT_MS = 1000 * 60 * 60 if IS_DEBUG else 3000  # 3000 ms


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
        job = win32job.CreateJobObject(None, 'LeetCode Env')
        currentProcess = win32api.GetCurrentProcess()
        jobInfo = win32job.QueryInformationJobObject(
            job, win32job.JobObjectExtendedLimitInformation)
        jobInfo["ProcessMemoryLimit"] = memoryLimit
        jobInfo["BasicLimitInformation"]["LimitFlags"] |=\
            win32job.JOB_OBJECT_LIMIT_PROCESS_MEMORY
        win32job.SetInformationJobObject(
            job, win32job.JobObjectExtendedLimitInformation, jobInfo)
        win32job.AssignProcessToJobObject(job, currentProcess)


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


def sub_f(q, fnc, *args, **kwargs):
    limitMemory(LEETCODE_MAX_MEMORY)
    setrecursionlimit(LEETCODE_MAX_RECURSION_DEPTH)
    disableStd()
    try:
        start = default_timer()
        res = fnc(*args, **kwargs)
        end = default_timer()
        q.put(((parseResult(res), end - start), None))
    except MemoryError:
        sys.exit(3)
    except Exception:
        error = getLastError()
        q.put((None, error))


def run_in_sub(fnc, *args, **kwargs):
    q = Queue()
    p = Process(target=sub_f, args=(q, fnc, *args), kwargs=kwargs)
    ret = None
    error = None
    p.start()
    enable = disableStd()
    try:
        ret, error = q.get(timeout=LEETCODE_MAX_TIMEOUT_MS * 2 / 1000)
    except Empty:
        code = p.exitcode
        if code in [1, 3, 0xC0000409, 0xC00000FD]:
            raise MemoryError()
        raise TimeoutError()
    finally:
        enable()
        if (p.is_alive()):
            p.terminate()
    p.join(1)
    if error:
        raise Exception(error)
    if ret[1] >= LEETCODE_MAX_TIMEOUT_MS:
        raise TimeoutError()
    return ret


def in_env(fnc: Callable):

    def execute(*args, **kwargs):
        executionInfo = {
            "Time": "-",
            "Execution Error": None,
            "Result": None,
            "Expected": None
        }
        res, runtime = None, -1
        try:
            res, runtime = run_in_sub(fnc, *args, **kwargs)
        except TimeoutError:
            executionInfo["Execution Error"] = "Time Limit Exceeded"
        except MemoryError:
            executionInfo["Execution Error"] = "Memory Limit Exceeded"
        except Exception as x:
            executionInfo["Execution Error"] = x.args[0][1]
        executionInfo["Time"] = "%.2f ms" % (runtime *
                                             1000) if runtime >= 0 else "N/A"
        executionInfo["Result"] = res
        return executionInfo

    return execute


MAX_PRINT_WIDTH_RESULT = sys.maxsize if IS_DEBUG else 200


def truncate(obj: Any, width: int):
    return textwrap.shorten(str(obj), width=width, placeholder="...")


def run(fnc: Callable,
        testCases: List[Tuple[List[Any], Any]],
        comparator=lambda x, y: x == y):
    wrapped_fnc = in_env(fnc)
    for no, test in enumerate(testCases):
        inputs, expected = test
        execution_info = wrapped_fnc(*inputs)
        execution_info["Expected"] = expected
        result = "\u001B[32mPass\u001B[0m" if \
            comparator(execution_info["Result"], expected)\
            and execution_info["Execution Error"] is None \
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
    else:
        print("Done")


""" HELPERS """


def any_order(a, b):
    return a and b and sorted(a) == sorted(b)


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
    def createTree(nums: List[int | None]):
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
        current, tree = [root], []
        while current.count(None) != len(current):
            tree.append(current)
            current = list(
                chain.from_iterable([i.left, i.right] if i else [None, None]
                                    for i in current))
        return _formated_tree([
            list(map(lambda x: x.val if x else None, level)) for level in tree
        ], emptyChar)

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, __o: object) -> bool:
        i, j = self, __o

        def nodes(root: Optional["TreeNode"]) -> List[int]:
            if not root:
                return []
            traversal, left, empty_count = [root], 0, 0
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

        return list(nodes(j)) == list(nodes(i))

    def __str__(self) -> str:
        return TreeNode._tree(self)


class ListNode:

    @staticmethod
    def createList(nums: List[int | None]):
        root = ListNode()
        current = root
        for i in nums:
            current.next = current = ListNode(i)
        return root.next

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, __o: object) -> bool:
        i, j = self, __o
        while i is not None and j is not None and i.val == j.val:
            i = i.next
            j = j.next
        return i is None and j is None

    def __str__(self) -> str:
        res = []
        i = self
        while i:
            res.append(i.val)
            i = i.next
        return str(res)
