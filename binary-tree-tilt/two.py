# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        self.total_tilt = 0

    def nodeTilt(self, root: TreeNode) -> int:
        if not root:
            return 0

        sum_left = self.nodeTilt(root.left)
        sum_right = self.nodeTilt(root.right)

        self.total_tilt += abs(sum_left - sum_right)
        return root.val + sum_left + sum_right

    def findTilt(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.nodeTilt(root)
        return self.total_tilt


# Runtime: 68 ms, faster than 67.58% of Python3 online submissions for Binary Tree Tilt.
# Memory Usage: 15.2 MB, less than 20.64% of Python3 online submissions for Binary Tree Tilt.
# based on reference solution
