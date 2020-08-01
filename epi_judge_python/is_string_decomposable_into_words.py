import functools
from typing import List, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook




# def decompose_into_dictionary_words(domain: str, dictionary: Set[str]) -> List[str]:
#     output = []
#     memo = [False for i in range(len(domain))]
#
#     def hasPathEnd(startIdx):
#         if startIdx == len(domain): return True
#         if memo[startIdx]: return False
#
#         val = ''
#         for i in range(startIdx, len(domain)):
#             val += domain[i]
#             if val in dictionary:
#                 output.append(val)
#                 if hasPathEnd(i+1): return True
#                 output.pop()
#         memo[startIdx] = True
#         return False
#
#     hasPathEnd(0)
#     return output


def decompose_into_dictionary_words(domain: str, dictionary: Set[str]) -> List[str]:
    last_length = [-1] * len(domain)
    for i in range(len(domain)):
        if domain[:i+1] in dictionary:
            last_length[i] = i + 1
            continue
        for j in range(i):
            if last_length[j] != -1 and domain[j+1:i+1] in dictionary:
                last_length[i] = i - j
                break
    print(last_length)
    decomps = []
    if last_length[-1] != -1:
        idx = len(domain) - 1
        while idx >= 0:
            decomps.append(domain[idx+1-last_length[idx]:idx +1])
            idx-=last_length[idx]
        decomps = decomps[::-1]
    return decomps




@enable_executor_hook
def decompose_into_dictionary_words_wrapper(executor, domain, dictionary,
                                            decomposable):
    result = executor.run(
        functools.partial(decompose_into_dictionary_words, domain, dictionary))

    if not decomposable:
        if result:
            raise TestFailure('domain is not decomposable')
        return

    if any(s not in dictionary for s in result):
        raise TestFailure('Result uses words not in dictionary')

    if ''.join(result) != domain:
        raise TestFailure('Result is not composed into domain')


if __name__ == '__main__':
    print(decompose_into_dictionary_words('amanaplanacanal', {'a','man','plan','canal','an'}))
    #
    # exit(
    #     generic_test.generic_test_main(
    #         'is_string_decomposable_into_words.py',
    #         'is_string_decomposable_into_words.tsv',
    #         decompose_into_dictionary_words_wrapper))
