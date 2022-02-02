# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import bisect


class Solution:
    def preOrderIsh(self, root: TreeNode) -> None:
        if not root:
            return 0

        bisect.insort_left(self.tree_list, root.val)

        self.preOrderIsh(root.left)
        self.preOrderIsh(root.right)

    def convertBST(self, root: TreeNode, top_level: bool = True) -> TreeNode:
        if not root:
            return None

        if top_level:
            self.tree_list = []
            self.preOrderIsh(root)

            self.tree_list_lookup = [None] * len(self.tree_list)
            acc = 0
            for i in range(len(self.tree_list) - 1, -1, -1):
                acc += self.tree_list[i]
                self.tree_list_lookup[i] = acc

        idx = bisect.bisect_left(self.tree_list, root.val)
        assert root.val == self.tree_list[idx]

        root.val = self.tree_list_lookup[idx]
        self.convertBST(root.left, False)
        self.convertBST(root.right, False)

        return root


# Runtime: 108 ms, faster than 23.82% of Python3 online submissions for Convert BST to Greater Tree.
# Memory Usage: 15.9 MB, less than 6.10% of Python3 online submissions for Convert BST to Greater Tree.
