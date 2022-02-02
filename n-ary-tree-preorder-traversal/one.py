"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: "Node", recursed=False) -> List[int]:
        if not root:
            return []

        if not recursed:
            self.porder = []

        self.porder.append(root.val)
        for child in root.children:
            self.preorder(child, True)

        return self.porder


# Runtime: 100 ms, faster than 46.64% of Python3 online submissions for N-ary Tree Preorder Traversal.
# Memory Usage: 17.6 MB, less than 5.26% of Python3 online submissions for N-ary Tree Preorder Traversal.
