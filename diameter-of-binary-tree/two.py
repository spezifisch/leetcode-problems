# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        self.cache = dict()

    def getDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        if root not in self.cache:
            self.cache[root] = 1 + max(
                self.getDepth(root.left), self.getDepth(root.right)
            )

        return self.cache[root]

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


# Runtime: 64 ms, faster than 31.76% of Python3 online submissions for Diameter of Binary Tree.
# Memory Usage: 15.6 MB, less than 5.33% of Python3 online submissions for Diameter of Binary Tree.
