# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    @staticmethod
    def searchValue(root: TreeNode, val: int) -> TreeNode:
        if root.val == val:
            return root
        if val < root.val and root.left is not None:
            return Solution.searchValue(root.left, val)
        if val > root.val and root.right is not None:
            return Solution.searchValue(root.right, val)
        return None
    
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return []
        
        return Solution.searchValue(root, val)
        
# Runtime: 84 ms, faster than 65.92% of Python3 online submissions for Search in a Binary Search Tree.
# Memory Usage: 15.1 MB, less than 5.30% of Python3 online submissions for Search in a Binary Search Tree.

