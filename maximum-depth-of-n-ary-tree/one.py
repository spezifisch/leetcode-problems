"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: "Node") -> int:
        if not root:
            return 0
        return 1 + max([0] + [self.maxDepth(child) for child in root.children])


# Runtime: 92 ms, faster than 38.49% of Python3 online submissions for Maximum Depth of N-ary Tree.
# Memory Usage: 17.5 MB, less than 5.30% of Python3 online submissions for Maximum Depth of N-ary Tree.
