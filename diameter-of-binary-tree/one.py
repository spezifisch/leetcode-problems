# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    @staticmethod
    def getDepth(root: TreeNode) -> int:
        if not root:
            return 0

        return 1 + max(Solution.getDepth(root.left), Solution.getDepth(root.right))

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0

        dias = []
        if root.left:
            dias.append(self.diameterOfBinaryTree(root.left))
        if root.right:
            dias.append(self.diameterOfBinaryTree(root.right))

        dias.append(self.getDepth(root.left) + self.getDepth(root.right))

        return max(dias)


# Runtime: 796 ms, faster than 6.02% of Python3 online submissions for Diameter of Binary Tree.
# Memory Usage: 16 MB, less than 5.33% of Python3 online submissions for Diameter of Binary Tree.
