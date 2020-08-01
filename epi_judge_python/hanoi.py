import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

NUM_PEGS = 3


def compute_tower_hanoi(num_rings: int) -> List[List[int]]:
    output = []

    def movePeg(ring, from_peg, to_peg, using_peg):
        if ring == 0:
            return

        movePeg(ring-1, from_peg, using_peg, to_peg)
        pegs[to_peg].append(pegs[from_peg].pop())
        output.append([from_peg,to_peg])
        movePeg(ring-1, using_peg, to_peg, from_peg)

    pegs = [[i for i in reversed(range(1,num_rings+1))]] + [[] for i in range(1, NUM_PEGS)]
    print(pegs)
    movePeg(num_rings, 0, 1, 2)
    return output


@enable_executor_hook
def compute_tower_hanoi_wrapper(executor, num_rings):
    pegs = [list(reversed(range(1, num_rings + 1)))
            ] + [[] for _ in range(1, NUM_PEGS)]

    result = executor.run(functools.partial(compute_tower_hanoi, num_rings))

    for from_peg, to_peg in result:
        if pegs[to_peg] and pegs[from_peg][-1] >= pegs[to_peg][-1]:
            raise TestFailure('Illegal move from {} to {}'.format(
                pegs[from_peg][-1], pegs[to_peg][-1]))
        pegs[to_peg].append(pegs[from_peg].pop())
    expected_pegs1 = [[], [], list(reversed(range(1, num_rings + 1)))]
    expected_pegs2 = [[], list(reversed(range(1, num_rings + 1))), []]
    if pegs not in (expected_pegs1, expected_pegs2):
        raise TestFailure('Pegs doesn\'t place in the right configuration')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('hanoi.py', 'hanoi.tsv',
                                       compute_tower_hanoi_wrapper))











    #
    #
    #
    # def compute_tower_hanoi_steps(num_rings_to_move, from_peg, to_peg, use_peg):
    #     if num_rings_to_move > 0:
    #         compute_tower_hanoi_steps(num_rings_to_move - 1, from_peg, use_peg, to_peg)
    #         pegs[to_peg].append(pegs[from_peg].pop())
    #         result.append([from_peg, to_peg])
    #         compute_tower_hanoi_steps(num_rings_to_move - 1, use_peg, to_peg, from_peg)
    #
    #
    # result = []
    # pegs = [list(reversed([i for i in range(1,num_rings+1)]))] + [[] for i in range(1,NUM_PEGS)]
    #
    # compute_tower_hanoi_steps(num_rings, 0, 1, 2)
    # return result
