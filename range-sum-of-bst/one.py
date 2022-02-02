# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0

        val = 0
        if L <= root.val <= R:
            val += root.val

        if root.left:
            val += self.rangeSumBST(root.left, L, R)
        if root.right:
            val += self.rangeSumBST(root.right, L, R)

        return val


# Runtime: 288 ms, faster than 41.84% of Python3 online submissions for Range Sum of BST.
# Memory Usage: 21.4 MB, less than 5.06% of Python3 online submissions for Range Sum of BST.
