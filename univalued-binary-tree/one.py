# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    @staticmethod
    def checkValues(val: TreeNode, root: TreeNode) -> bool:
        left_ok = right_ok = True
        if root.val != val:
            return False
        if root.left is not None:
            left_ok = Solution.checkValues(val, root.left)
        if root.right is not None:
            right_ok = Solution.checkValues(val, root.right)
            
        return left_ok and right_ok
    
    def isUnivalTree(self, root: TreeNode) -> bool:
        return Solution.checkValues(root.val, root)
    
# Runtime: 40 ms, faster than 41.89% of Python3 online submissions for Univalued Binary Tree.
# Memory Usage: 13.2 MB, less than 5.36% of Python3 online submissions for Univalued Binary Tree.

