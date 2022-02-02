# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        a = self.inOrderLeaf(root1)
        b = self.inOrderLeaf(root2)
        return a == b

    def inOrderLeaf(self, root: TreeNode) -> List[int]:
        if not root:
            return

        leaves = []
        if root.left:
            leaves += self.inOrderLeaf(root.left)
        if root.right:
            leaves += self.inOrderLeaf(root.right)

        if not root.left and not root.right:
            leaves += [root.val]

        return leaves


# Runtime: 40 ms, faster than 54.31% of Python3 online submissions for Leaf-Similar Trees.
# Memory Usage: 13.1 MB, less than 5.32% of Python3 online submissions for Leaf-Similar Trees.
