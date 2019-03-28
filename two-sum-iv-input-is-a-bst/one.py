# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    @staticmethod
    def containsValue(root: TreeNode, val: int, exclude: TreeNode) -> bool:
        if not root:
            return False
        if val < root.val:
            return Solution.containsValue(root.left, val, exclude)
        if val > root.val:
            return Solution.containsValue(root.right, val, exclude)
        if root == exclude:
            return False
        return True
    
    def findTarget(self, root: TreeNode, k: int, orig_root: TreeNode = None) -> bool:
        if orig_root is None:
            orig_root = root
        
        if not root:
            return False
        
        wanted = k - root.val
        if self.containsValue(orig_root, wanted, exclude=root):
            return True
        
        if self.findTarget(root.left, k, orig_root):
            return True
        if self.findTarget(root.right, k, orig_root):
            return True
        
        return False
    
# Runtime: 96 ms, faster than 65.66% of Python3 online submissions for Two Sum IV - Input is a BST.
# Memory Usage: 15.5 MB, less than 5.00% of Python3 online submissions for Two Sum IV - Input is a BST.

