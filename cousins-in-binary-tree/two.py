# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class MetaNode:
    def __init__(self, x, parent: TreeNode, level: int):
        self.val = x
        self.parent = parent
        self.level = level


class Solution:
    @staticmethod
    def getNode(
        root: TreeNode,
        val: int,
        max_level: int = None,
        parent: TreeNode = None,
        level: int = 1,
    ) -> MetaNode:
        if not root:
            return None

        if root.val == val:
            return MetaNode(val, parent, level)

        if max_level is not None and level > max_level:
            return None

        if root.left:
            ret = Solution.getNode(root.left, val, max_level, root, level + 1)
            if ret is not None:
                return ret

        if root.right:
            return Solution.getNode(root.right, val, max_level, root, level + 1)

        return None

    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        x_meta = self.getNode(root, x)
        y_meta = self.getNode(root, y, x_meta.level)
        if y_meta is None:
            return False

        return x_meta.level == y_meta.level and x_meta.parent != y_meta.parent


# Runtime: 40 ms, faster than 58.20% of Python3 online submissions for Cousins in Binary Tree.
# Memory Usage: 13.2 MB, less than 5.08% of Python3 online submissions for Cousins in Binary Tree.
