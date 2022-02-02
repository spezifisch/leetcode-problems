# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.sum_cache = dict()
    
    def subTreeSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        if root not in self.sum_cache:
            self.sum_cache[root] = root.val + self.subTreeSum(root.left) + self.subTreeSum(root.right)
            
        return self.sum_cache[root]
    
    def nodeTilt(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        return abs(self.subTreeSum(root.left) - self.subTreeSum(root.right))
    
    def findTilt(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        return self.nodeTilt(root) + self.findTilt(root.left) + self.findTilt(root.right)
    
# Runtime: 88 ms, faster than 24.52% of Python3 online submissions for Binary Tree Tilt.
# Memory Usage: 15.3 MB, less than 11.11% of Python3 online submissions for Binary Tree Tilt.

