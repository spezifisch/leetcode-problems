"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root: "Node", recursed=False) -> List[int]:
        if not root:
            return []

        if not recursed:
            self.porder = []

        for child in root.children:
            self.postorder(child, recursed=True)

        self.porder.append(root.val)
        if not recursed:
            return self.porder

        return None


# Runtime: 100 ms, faster than 43.26% of Python3 online submissions for N-ary Tree Postorder Traversal.
# Memory Usage: 17.5 MB, less than 6.03% of Python3 online submissions for N-ary Tree Postorder Traversal.
