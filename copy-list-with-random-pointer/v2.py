"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None

        node = head
        prev_node = None

        # let's exploit the fact that node objects are mutable and we can just add a "copy" field to each one
        # first pass: go through the list linearly and create copies
        while node:
            # create copy of this node
            node.copy = Node(node.val)

            if prev_node is not None:
                prev_node.copy.next = node.copy
            else:
                prev_node = head

            prev_node = node
            node = node.next

        # 2nd pass: resolve random references
        node = head
        while node:
            if node.random:
                node.copy.random = node.random.copy

            node = node.next

        return head.copy


# Runtime: 40 ms, faster than 81.70% of Python3 online submissions for Copy List with Random Pointer.
# Memory Usage: 15 MB, less than 55.97% of Python3 online submissions for Copy List with Random Pointer.
