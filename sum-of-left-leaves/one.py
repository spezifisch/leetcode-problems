# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0

        val = 0
        if root.left:
            if not root.left.left and not root.left.right:
                val += root.left.val
            else:
                val += self.sumOfLeftLeaves(root.left)
        if root.right:
            val += self.sumOfLeftLeaves(root.right)

        return val


# Runtime: 40 ms, faster than 76.60% of Python3 online submissions for Sum of Left Leaves.
# Memory Usage: 14 MB, less than 5.32% of Python3 online submissions for Sum of Left Leaves.
