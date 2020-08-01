from typing import Optional

from list_node import ListNode
from test_framework import generic_test


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(head: ListNode, k: int) -> Optional[ListNode]:
    dummy_head = prev = ListNode(0, head)
    curr, fast = head, head

    for _ in range(k):
        fast = fast.next

    while fast:
        prev,curr,fast = prev.next,curr.next,fast.next

    prev.next = curr.next

    return dummy_head.next



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('delete_kth_last_from_list.py',
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
