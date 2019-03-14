# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    @staticmethod
    def getInsertNode(root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None
        
        if root.left and val < root.val:
            return Solution.getInsertNode(root.left, val)
        elif root.right and val > root.val:
            return Solution.getInsertNode(root.right, val)
        
        return root
    
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None
        
        new_node = TreeNode(val)
        fc = self.getInsertNode(root, val)
        if fc.val > val:
            fc.left = new_node
        else:
            fc.right = new_node
            
        return root

# Runtime: 144 ms, faster than 26.69% of Python3 online submissions for Insert into a Binary Search Tree.
# Memory Usage: 15.2 MB, less than 5.32% of Python3 online submissions for Insert into a Binary Search Tree.

