# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
from typing import Iterable


class Moo(Iterable):
    def __init__(self, n: Optional[ListNode]):
        self.n = n

    def __iter__(self):
        return self

    def __next__(self) -> ListNode:
        x = self.n
        if x is None:
            raise StopIteration()
        self.n = self.n.next
        return x


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodegens = [Moo(x) for x in lists]

        first_node = None
        last_node = None
        for node in heapq.merge(*nodegens, key=lambda x: x.val):
            if first_node is None:
                first_node = node
            if last_node is not None:
                last_node.next = node

            last_node = node

        return first_node


# Runtime: 131 ms, faster than 58.72% of Python3 online submissions for Merge k Sorted Lists.
# Memory Usage: 20.1 MB, less than 5.43% of Python3 online submissions for Merge k Sorted Lists.
