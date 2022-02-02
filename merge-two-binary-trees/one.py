# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    @staticmethod
    def safeGet(obj, attr):
        return getattr(obj, attr, None)

    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and not t2:
            return None

        t = TreeNode(0)
        if t1:
            t.val += t1.val
        if t2:
            t.val += t2.val

        t.left = self.mergeTrees(
            Solution.safeGet(t1, "left"), Solution.safeGet(t2, "left")
        )
        t.right = self.mergeTrees(
            Solution.safeGet(t1, "right"), Solution.safeGet(t2, "right")
        )

        return t


# Runtime: 132 ms, faster than 17.58% of Python3 online submissions for Merge Two Binary Trees.
# Memory Usage: 14.5 MB, less than 5.13% of Python3 online submissions for Merge Two Binary Trees.
