# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        n = self.inOrder(root)
        ret_root = TreeNode(n[0])
        node = ret_root
        for i in range(1, len(n)):
            node.right = TreeNode(n[i])
            node = node.right
            
        return ret_root
        
    def inOrder(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        ret = []
        if root.left:
            ret += self.inOrder(root.left)
        ret += [root.val]
        if root.right:
            ret += self.inOrder(root.right)
            
        return ret
        
# Runtime: 168 ms, faster than 24.27% of Python3 online submissions for Increasing Order Search Tree.
# Memory Usage: 13.2 MB, less than 5.97% of Python3 online submissions for Increasing Order Search Tree.

