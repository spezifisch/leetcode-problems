# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        self.ret = list()

    def levelOrderRecurse(self, root: TreeNode, depth: int) -> None:
        if not root:
            return

        if depth >= len(self.ret):
            self.ret.append([root.val])
        else:
            self.ret[depth].append(root.val)

        self.levelOrderRecurse(root.left, depth + 1)
        self.levelOrderRecurse(root.right, depth + 1)

    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        self.levelOrderRecurse(root, 0)

        return self.ret[::-1]


# Runtime: 44 ms, faster than 67.78% of Python3 online submissions for Binary Tree Level Order Traversal II.
# Memory Usage: 13.8 MB, less than 5.23% of Python3 online submissions for Binary Tree Level Order Traversal II.
