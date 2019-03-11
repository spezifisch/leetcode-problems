# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    @staticmethod
    def checkValues(val: TreeNode, root: TreeNode) -> bool:
        if root.val != val:
            return False
        if root.left is not None:
            if not Solution.checkValues(val, root.left):
                return False
        if root.right is not None:
            if not Solution.checkValues(val, root.right):
                return False
            
        return True
    
    def isUnivalTree(self, root: TreeNode) -> bool:
        return Solution.checkValues(root.val, root)
    
# Runtime: 40 ms, faster than 41.89% of Python3 online submissions for Univalued Binary Tree.
# Memory Usage: 13.1 MB, less than 5.36% of Python3 online submissions for Univalued Binary Tree.

