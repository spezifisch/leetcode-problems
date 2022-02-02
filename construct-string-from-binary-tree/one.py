# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if not t:
            return ""

        left_str = self.tree2str(t.left)
        right_str = self.tree2str(t.right)

        if left_str or right_str:
            left_str = "(" + left_str + ")"

        if right_str:
            right_str = "(" + right_str + ")"

        return str(t.val) + left_str + right_str


# Runtime: 60 ms, faster than 83.57% of Python3 online submissions for Construct String from Binary Tree.
# Memory Usage: 15.5 MB, less than 5.17% of Python3 online submissions for Construct String from Binary Tree.
