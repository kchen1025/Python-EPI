from typing import List

from test_framework import generic_test


def palindrome_decompositions(text: str) -> List[List[str]]:
    out = []
    buff = []

    def helper(startIdx):
        if startIdx >= len(text):
            out.append(buff.copy())
            return

        for i in range(startIdx, len(text)):
            currStr = text[startIdx:i+1]

            if isPalindrome(currStr):
                buff.append(currStr)
                helper(i+1)
                buff.pop()

    helper(0)
    return out

def isPalindrome(arr):
    if len(arr) == 0:
        return True

    p1,p2 = 0,len(arr)-1

    while p1 <= p2:
        if arr[p1] != arr[p2]:
            return False
        p1+=1
        p2-=1
    return True


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    # print(palindrome_decompositions('020445'))
    exit(
        generic_test.generic_test_main(
            'enumerate_palindromic_decompositions.py',
            'enumerate_palindromic_decompositions.tsv',
            palindrome_decompositions, comp))
