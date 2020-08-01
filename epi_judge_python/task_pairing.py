import collections
from typing import List

from test_framework import generic_test

PairedTasks = collections.namedtuple('PairedTasks', ('task_1', 'task_2'))


def optimum_task_assignment(task_durations: List[int]) -> List[PairedTasks]:
    output = []
    task_durations.sort()

    start = 0
    end = len(task_durations)-1

    while start <= end:
        output.append(PairedTasks(task_durations[start], task_durations[end]))
        start+=1
        end-=1

    return output


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('task_pairing.py', 'task_pairing.tsv',
                                       optimum_task_assignment))
