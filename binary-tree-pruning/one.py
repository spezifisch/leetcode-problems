# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        if not self.subTreeSum(root):
            return None
        
        return root
    
    @staticmethod
    def subTreeSum(root: TreeNode) -> int:
        ret = root.val
        
        if root.left:
            val = Solution.subTreeSum(root.left)
            ret += val
            
            if val == 0:
                root.left = None
        if root.right:
            val = Solution.subTreeSum(root.right)
            ret += val
            
            if val == 0:
                root.right = None
                
        return ret

# Runtime: 36 ms, faster than 78.99% of Python3 online submissions for Binary Tree Pruning.
# Memory Usage: 13.1 MB, less than 7.25% of Python3 online submissions for Binary Tree Pruning.

