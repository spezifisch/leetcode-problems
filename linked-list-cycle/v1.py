# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodes = set()
        node = head
        while node:
            nodes.add(node)
            node = node.next
            if node in nodes:
                return True

        return False


# Runtime: 48 ms, faster than 98.31% of Python3 online submissions for Linked List Cycle.
# Memory Usage: 18 MB, less than 13.44% of Python3 online submissions for Linked List Cycle.
