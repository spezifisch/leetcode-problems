"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root: "Node") -> List[int]:
        if not root:
            return []

        if not getattr(self, "porder", None):
            self.porder = []

        # leaf
        if not len(root.children):
            self.porder.append(root.val)
            return self.porder

        # parent
        for child in root.children:
            self.postorder(child)

        self.porder.append(root.val)

        return self.porder


# Runtime: 108 ms, faster than 16.02% of Python3 online submissions for N-ary Tree Postorder Traversal.
# Memory Usage: 17.5 MB, less than 6.03% of Python3 online submissions for N-ary Tree Postorder Traversal.
