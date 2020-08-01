from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L: ListNode, start: int,finish: int) -> Optional[ListNode]:
    if not L: return

    dummy_head = ListNode(-1)
    dummy_head.next = L

    sublist_head, curs, curs_next = dummy_head, L, L.next
    node_count = 1

    while node_count < start:
        sublist_head, curs, curs_next = sublist_head.next, curs.next, curs_next.next
        node_count+=1

    for _ in range(finish - start):
        curs.next = curs_next.next
        curs_next.next = sublist_head.next
        sublist_head.next = curs_next
        curs_next = curs.next

    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))






























#
# temp = sublist_iter.next
# sublist_iter.next = temp.next
# temp.next = sublist_head.next
# sublist_head.next = temp
