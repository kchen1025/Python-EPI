import functools

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

def getLength(node):
    curs,step = node,0
    while curs:
        step+=1
        curs = curs.next
    return step


def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> ListNode:
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
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(functools.partial(overlapping_no_cycle_lists, l0,
                                            l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_terminated_lists_overlap.py',
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
