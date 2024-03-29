# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        if mid > 0:
            root.left = self.sortedArrayToBST(nums[:mid])
        if mid < len(nums) - 1:
            root.right = self.sortedArrayToBST(nums[mid + 1 :])

        return root


# Runtime: 64 ms, faster than 82.01% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
# Memory Usage: 15.5 MB, less than 5.70% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
