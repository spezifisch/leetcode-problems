# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.sum = 0
        
    def add_sum(self, path: List[int]) -> None:
        factor = 1
        num = 0
        for bdigit in path[::-1]:
            if bdigit:
                num += bdigit * factor
            
            factor <<= 1
            
        self.sum += num
        
    def sumRootToLeaf(self, root: TreeNode, path: List[int] = []) -> int:
        if not root:
            return 0
        
        path = path + [root.val]
        if not root.left and not root.right:
            self.add_sum(path)
        else:
            self.sumRootToLeaf(root.left, path)
            self.sumRootToLeaf(root.right, path)

        return self.sum
    
# Runtime: 48 ms, faster than 100.00% of Python3 online submissions for Sum of Root To Leaf Binary Numbers.
# Memory Usage: 13.6 MB, less than 100.00% of Python3 online submissions for Sum of Root To Leaf Binary Numbers.

