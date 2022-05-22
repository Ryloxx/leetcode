from typing import Any, Callable, List, Tuple


def run(fnc: Callable, testCases: List[Tuple[List[Any], Any]], unpacker=None):
    for no, test in enumerate(testCases):
        inputs, expected = test
        got = fnc(*inputs)
        if unpacker is not None:
            got = unpacker(got)
        if got != expected:
            sinput = "\n\t".join(map(str, inputs))
            print(
                f"Invalid for test {no}\n\
                    - Inputs: {sinput}\n\
                    - Expected: {expected}\n\
                    - Got: {got}"
            )
            break


print("Success")
