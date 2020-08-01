from typing import List

from test_framework import generic_test


def has_three_sum(A: List[int], t: int) -> bool:
    A.sort()

    for i in range(len(A)):
        first,last = i,len(A)-1

        while first <= last:
            curr_sum = A[i]+A[first]+A[last]
            if curr_sum > t:
                last-=1
            elif curr_sum < t:
                first+=1
            else:
                return True
    return False
    # A.sort()
    #
    # for i in A:
    #     if has_two_sum(A, t-i):
    #         return True
    # return False

# def has_two_sum(A, t):
#     p1,p2 = 0, len(A) - 1
#
#     while p1 <= p2:
#         sumVal = A[p1] + A[p2]
#
#         if sumVal < t:
#             p1+=1
#         elif sumVal > t:
#             p2-=1
#         else:
#             return True
#     return False

if __name__ == '__main__':

    exit(
        generic_test.generic_test_main('three_sum.py', 'three_sum.tsv',
                                       has_three_sum))













































#
#     A.sort()
#     return any([has_two_sum(A, t - i) for i in A])
#
# def has_two_sum(A, t):
#     i,j = 0,len(A)-1
#
#     while i <= j:
#         if A[i] + A[j] < t:
#             i+=1
#         elif A[i] + A[j] > t:
#             j-=1
#         else:
#             return True
#     return False
