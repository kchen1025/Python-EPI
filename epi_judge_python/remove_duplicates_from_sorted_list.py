from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def remove_duplicates(L: ListNode) -> Optional[ListNode]:
    curr = runner = L

    while runner:
        if curr.data == runner.data:
            runner = runner.next
        else:
            curr.next = runner
            curr = runner
    if curr: curr.next = runner
    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'remove_duplicates_from_sorted_list.py',
            'remove_duplicates_from_sorted_list.tsv', remove_duplicates))
