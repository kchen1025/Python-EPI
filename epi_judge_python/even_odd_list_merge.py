from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def even_odd_merge(head: ListNode) -> Optional[ListNode]:
    if not head: return

    evenQ, oddQ = [],[]
    count, curr = 0, head

    while curr:
        if count != 0 and count % 2 == 0:
            evenQ.append(curr)
        elif count % 2 == 1:
            oddQ.append(curr)
        count += 1
        curr = curr.next

    if count == 1: return head
    curr = head

    for node in (evenQ+oddQ):
        curr.next = node
        curr = curr.next
    curr.next = None
    return head



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_list_merge.py',
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
