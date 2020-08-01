from typing import List

from test_framework import generic_test


def multiply(a1: List[int], a2: List[int]) -> List[int]:
    out = [0] * (len(a1) + len(a2))
    isNeg = (a1[0] < 0) ^ (a2[0] < 0)

    a1[0] = abs(a1[0])
    a2[0] = abs(a2[0])

    for i in reversed(range(len(a1))):
        for j in reversed(range(len(a2))):
            out[i+j+1] += (a2[j] * a1[i])
            out[i+j] += (out[i+j+1] // 10)
            out[i+j+1] %= 10

    #remove leading zeroes
    c = 0
    while c < len(out) and out[c] == 0:
        c+=1

    if c == len(out):
        return [0]

    out = out[c:]

    if isNeg:
        first = out[0] * -1
        return [first]+out[1:]
    else:
        return out




if __name__ == '__main__':
    # print(multiply([-3,4],[1,2,3]))

    exit(
        generic_test.generic_test_main('int_as_array_multiply.py',
                                       'int_as_array_multiply.tsv', multiply))



































#
#
#
#     out = [0] * (len(a1) + len(a2))
#     isNeg = (a1[0] < 0) ^ (a2[0] < 0)
#
#     a1[0],a2[0] = abs(a1[0]),abs(a2[0])
#
#     for i in reversed(range(len(a1))):
#         for j in reversed(range(len(a2))):
#             out[i+j+1] += (a1[i] * a2[j])
#             out[i+j] += (out[i+j+1]//10)
#             out[i+j+1] %= 10
#
#
#     final = removeZeros(out)
#     if isNeg: final[0] *= -1
#     return final
#
# def removeZeros(out):
#     i = 0
#     while i < len(out) and out[i] == 0:
#         i+=1
#     if i == len(out): return [0]
#     return [x for i,x in enumerate(out[i:])]
