from typing import List

from test_framework import generic_test

def num_combinations_for_final_score(final_score: int,play_scores: List[int]) -> int:
    memo = [[1]+[0 for i in range(final_score)] for j in range(len(play_scores))]

    for i in range(len(play_scores)):
        for j in range(1, final_score+1):
            if i > 0:
                memo[i][j] += memo[i-1][j]
            if j - play_scores[i] >= 0:
                memo[i][j] += memo[i][j-play_scores[i]]
    return memo[-1][-1]


if __name__ == '__main__':


    exit(
        generic_test.generic_test_main('number_of_score_combinations.py',
                                       'number_of_score_combinations.tsv',
                                       num_combinations_for_final_score))
