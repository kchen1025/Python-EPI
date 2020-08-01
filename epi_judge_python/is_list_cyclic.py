import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook



def has_cycle(head: ListNode) -> Optional[ListNode]:
    #fast slow pointer until you find a cycle (or none exists)
    fast, slow = head, head

    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next

        if fast is slow:
            break;

    if fast is not slow:
        return None

    # if one exists, find length of it
    cycleLength = 1
    fast = fast.next
    while fast is not slow:
        cycleLength += 1
        fast = fast.next

    # use fast/slow again but first iterating fast to length of cycle spaces away
    # then iterating both at same pace until match
    fast,slow = head,head
    for _ in range(cycleLength):
        fast = fast.next

    while fast is not slow:
        fast = fast.next
        slow = slow.next
    return fast


@enable_executor_hook
def has_cycle_wrapper(executor, head, cycle_idx):
    cycle_length = 0
    if cycle_idx != -1:
        if head is None:
            raise RuntimeError('Can\'t cycle empty list')
        cycle_start = None
        cursor = head
        while cursor.next is not None:
            if cursor.data == cycle_idx:
                cycle_start = cursor
            cursor = cursor.next
            cycle_length += 1 if cycle_start is not None else 0

        if cursor.data == cycle_idx:
            cycle_start = cursor
        if cycle_start is None:
            raise RuntimeError('Can\'t find a cycle start')
        cursor.next = cycle_start
        cycle_length += 1

    result = executor.run(functools.partial(has_cycle, head))

    if cycle_idx == -1:
        if result is not None:
            raise TestFailure('Found a non-existing cycle')
    else:
        if result is None:
            raise TestFailure('Existing cycle was not found')
        cursor = result
        while True:
            cursor = cursor.next
            cycle_length -= 1
            if cursor is None or cycle_length < 0:
                raise TestFailure(
                    'Returned node does not belong to the cycle or is not the closest node to the head'
                )
            if cursor is result:
                break

    if cycle_length != 0:
        raise TestFailure(
            'Returned node does not belong to the cycle or is not the closest node to the head'
        )


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_list_cyclic.py',
                                       'is_list_cyclic.tsv',
                                       has_cycle_wrapper))


                                # def cycle_len(end):
                                #     start, step = end, 0
                                #     while True:
                                #         start = start.next
                                #         step+=1
                                #         if start is end:
                                #             return step
                                #
                                # fast = slow = head
                                #
                                # while fast and fast.next:
                                #     slow, fast = slow.next, fast.next.next
                                #
                                #     if slow is fast:
                                #         cycle_len_advanced_iter = head
                                #         for _ in range(cycle_len(slow)):
                                #             cycle_len_advanced_iter = cycle_len_advanced_iter.next
                                #
                                #         it = head
                                #         while it is not cycle_len_advanced_iter:
                                #             it = it.next
                                #             cycle_len_advanced_iter = cycle_len_advanced_iter.next
                                #         return it
                                # return None
