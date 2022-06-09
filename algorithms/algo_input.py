from multiprocessing import Process, Queue
import os
from queue import Empty
import sys
from sys import setrecursionlimit
import textwrap
from timeit import default_timer
from traceback import format_tb
from typing import Any, Callable, List, Tuple

IS_DEBUG = "DEBUG" in os.environ \
        and os.environ["DEBUG"].lower() == "true"

LEETCODE_MAX_RECURSION_DEPTH = 20_000
LEETCODE_MAX_MEMORY = 100 * 1024 * 1024  # 100 MB
LEETCODE_MAX_TIMEOUT_MS = 1000 * 60 * 60 if IS_DEBUG else 3000  # 3000 ms


def disableStd():
    null = open(os.devnull)
    temp = sys.stderr, sys.stdout
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
              f"- {result}"
              f"- {execution_info}")
    else:
        print("Done")


def any_order(a, b):
    return a and b and sorted(a) == sorted(b)
