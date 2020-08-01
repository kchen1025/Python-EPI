from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def cyclically_right_shift_list(L: ListNode, k: int) -> Optional[ListNode]:
    if not L:
        return L

    head = L

    new_tail, length = L, 1
    while new_tail.next:
        length += 1
        new_tail = new_tail.next

    k = k % length
    if k == 0:
        return head

    new_tail.next = head
    new_head = head
    for _ in range(length - k):
        new_head = new_head.next
        new_tail = new_tail.next

    new_tail.next = None
    return new_head



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('list_cyclic_right_shift.py',
                                       'list_cyclic_right_shift.tsv',
                                       cyclically_right_shift_list))
