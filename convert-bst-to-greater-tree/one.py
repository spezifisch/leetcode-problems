# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    @staticmethod
    def getSumGT(root: TreeNode, val: int) -> int:
        if not root:
            return 0

        ret = 0
        if root.val > val:
            ret += root.val
            ret += Solution.getSumGT(root.left, val)
            ret += Solution.getSumGT(root.right, val)
        else:
            ret += Solution.getSumGT(root.right, val)

        return ret

    def convertBST(self, root: TreeNode, orig_root: TreeNode = None) -> TreeNode:
        if not root:
            return None
        if orig_root is None:
            orig_root = root

        new_root = TreeNode(root.val + self.getSumGT(orig_root, root.val))
        new_root.left = self.convertBST(root.left, orig_root)
        new_root.right = self.convertBST(root.right, orig_root)

        return new_root


# Time Limit Exceeded
