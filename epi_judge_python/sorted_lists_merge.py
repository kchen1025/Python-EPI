from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def merge_two_sorted_lists(L1: Optional[ListNode],
                           L2: Optional[ListNode]) -> Optional[ListNode]:
    c1 = L1
    c2 = L2
    out = ListNode(-1)
    outHead = out

    while c1 and c2:
        if c1.data < c2.data:
            out.next = c1
            c1 = c1.next
        else:
            out.next = c2
            c2 = c2.next
        out = out.next

    if c1:
        out.next = c1
    else:
        out.next = c2


    return outHead.next



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
