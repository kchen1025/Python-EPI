from test_framework import generic_test


def levenshtein_distance(A: str, B: str) -> int:
    memo = [[0] * (len(A) + 1)  for _ in range(len(B)+1)]
    memo[0] = [i for i in range(len(A)+1)]
    for i in range(len(B)+1):
        memo[i][0] = i

    # loop through arr
    for i in range(1,len(B)+1):
        for j in range(1, len(A)+1):
            # if current chars equal
            if A[j-1] == B[i-1]:
                memo[i][j] = memo[i-1][j-1]
            else:
                memo[i][j] = min(memo[i-1][j], memo[i][j-1], memo[i-1][j-1]) + 1
    return memo[-1][-1]



if __name__ == '__main__':
    print(levenshtein_distance('GCTACACGCAGTTGCCTCGAGGAAACAAGCGCAATCGGATCGCGCATCCACACCACGACCCTGTAA','GGGGATTCGGCATGGCGTAGGGGAATTGCTGAACGACACTCGTGCATTTAAGGGGGAACTATTACAG'))

    # print(levenshtein_distance('yeet','yeah'))
    exit(
        generic_test.generic_test_main('levenshtein_distance.py',
                                       'levenshtein_distance.tsv',
                                       levenshtein_distance))
