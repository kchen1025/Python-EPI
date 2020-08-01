import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

def getCycleLength(node):
    curs, step = node.next, 1

    while curs is not node:
        step+=1
        curs = curs.next
    return step

# maintain 2 pointers. if they overlap, you have a cycle.
# get its length, then iterate from beginning to find total length of list as before
# if there is no overlap, then p2 will be null and you just return p1 count
def getLength(node):
    p1 = p2 = node
    step = 0

    while p2 and p2.next:
        p1 = p1.next
        p2 = p2.next.next
        step += 1

        # cycle found
        if p1 is p2:
            advance_point = node
            cycleLength = getCycleLength(p1)
            for _ in range(cycleLength):
                advance_point = advance_point.next
            it, count = node,0

            while it is not advance_point:
                count+=1
                advance_point = advance_point.next
                it = it.next
            return count + cycleLength

    # if p2 hit the end, finish counting p1
    while p1:
        step+=1
        p1 = p1.next
    return step


def overlapping_lists(l0: ListNode, l1: ListNode) -> Optional[ListNode]:
    print(l0,l1)
    # find lengths of each list
    length1 = getLength(l0)
    length2 = getLength(l1)

    if(length1 > length2):
        l0,l1 = l1,l0

    # take difference, and iterate longer list forward by different
    for _ in range(abs(length2 - length1)):
        l1 = l1.next

    # advance both list pointers at the same time until meet
    while l0 and l1 and l0 is not l1:
        l0 = l0.next
        l1 = l1.next

    # return any list pointer (null if no overlap)
    return l0


@enable_executor_hook
def overlapping_lists_wrapper(executor, l0, l1, common, cycle0, cycle1):
    if common:
        if not l0:
            l0 = common
        else:
            it = l0
            while it.next:
                it = it.next
            it.next = common

        if not l1:
            l1 = common
        else:
            it = l1
            while it.next:
                it = it.next
            it.next = common

    if cycle0 != -1 and l0:
        last = l0
        while last.next:
            last = last.next
        it = l0
        for _ in range(cycle0):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    if cycle1 != -1 and l1:
        last = l1
        while last.next:
            last = last.next
        it = l1
        for _ in range(cycle1):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    common_nodes = set()
    it = common
    while it and id(it) not in common_nodes:
        common_nodes.add(id(it))
        it = it.next

    result = executor.run(functools.partial(overlapping_lists, l0, l1))

    if not (id(result) in common_nodes or (not common_nodes and not result)):
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_lists_overlap.py',
                                       'do_lists_overlap.tsv',
                                       overlapping_lists_wrapper))
