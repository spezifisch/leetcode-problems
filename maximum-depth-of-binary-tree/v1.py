# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# Runtime: 72 ms, faster than 21.63% of Python3 online submissions for Maximum Depth of Binary Tree.
# Memory Usage: 16.3 MB, less than 18.15% of Python3 online submissions for Maximum Depth of Binary Tree.
