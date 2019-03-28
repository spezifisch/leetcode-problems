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
        
        left_slice = right_slice = None
        if mid > 0:
            left_slice = nums[:mid]
        if mid < len(nums) - 1:
            right_slice = nums[mid+1:]
            
        root = TreeNode(nums[mid])
        if left_slice:
            root.left = self.sortedArrayToBST(left_slice)
        if right_slice:
            root.right = self.sortedArrayToBST(right_slice)
            
        return root
    
# Runtime: 64 ms, faster than 82.01% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
# Memory Usage: 15.5 MB, less than 5.70% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.

