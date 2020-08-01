from test_framework import generic_test


def rabin_karp(haystack: str, needle: str) -> int:
    if len(needle) > len(haystack):
        return -1

    # helper functions for quick computation of hash code
    ned_to_int = lambda i : ord(needle[i]) - ord('a')
    hay_to_int = lambda i : ord(haystack[i]) - ord('a')

    # first compute the beginning of both strings
    needleCode, hayCode = 0,0

    # loop to the length of the needle, we are multiplying the current code by 26 and adding the new value because of the nature of the polynomial
    # which has 26**exp in reverse
    for i in range(len(needle)):
        needleCode = needleCode * 26 + ned_to_int(i)
        hayCode = hayCode * 26 + hay_to_int(i)

    # if equal, first occurence is at 0
    if hayCode == needleCode: return 0

    # now we loop until the end of the string and roll the hash in O(1) time
    aL = pow(26, len(needle)-1)
    for i in range(1, len(haystack) - len(needle) + 1):
        # roll the hash
        hayCode = (hayCode - (hay_to_int(i-1) * aL)) * 26 + hay_to_int(i+len(needle)-1)

        # if equal, return
        if needleCode == hayCode:
            return i
    return -1



if __name__ == '__main__':
    print(rabin_karp('A','A'))
    print(rabin_karp('abcd','cd'))
    exit(
        generic_test.generic_test_main('substring_match.py',
                                       'substring_match.tsv', rabin_karp))
