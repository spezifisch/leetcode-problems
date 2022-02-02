# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        first_bigger = len(preorder)
        for i, elem in enumerate(preorder[1:]):
            if elem > root.val:
                first_bigger = i
                break

        lower_slice = preorder[1:][:first_bigger]
        bigger_slice = preorder[1:][first_bigger:]
        if len(lower_slice):
            root.left = self.bstFromPreorder(lower_slice)
        if len(bigger_slice):
            root.right = self.bstFromPreorder(bigger_slice)

        return root
