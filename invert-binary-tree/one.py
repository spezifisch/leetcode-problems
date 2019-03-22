# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        tmp = root.left
        root.left = root.right
        root.right = tmp
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
    
# Runtime: 40 ms, faster than 46.67% of Python3 online submissions for Invert Binary Tree.
# Memory Usage: 13.2 MB, less than 5.74% of Python3 online submissions for Invert Binary Tree.

