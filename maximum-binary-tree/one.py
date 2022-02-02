# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not len(nums):
            return

        root = TreeNode(max(nums))
        max_pos = nums.index(root.val)

        root.left = self.constructMaximumBinaryTree(nums[:max_pos])
        root.right = self.constructMaximumBinaryTree(nums[max_pos + 1 :])

        return root


# Runtime: 156 ms, faster than 68.87% of Python3 online submissions for Maximum Binary Tree.
# Memory Usage: 13.5 MB, less than 5.00% of Python3 online submissions for Maximum Binary Tree.
