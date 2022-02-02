# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import bisect


class Solution:
    def buildSortedTreeList(self, root: TreeNode) -> None:
        if not root:
            return 0

        self.buildSortedTreeList(root.left)
        self.tree_list.append(root.val)
        self.buildSortedTreeList(root.right)

    def convertBST(self, root: TreeNode, top_level: bool = True) -> TreeNode:
        if not root:
            return None

        if top_level:
            self.tree_list = []
            self.buildSortedTreeList(root)

            # cumulative sum of the current element and all elements to its right
            self.new_val = dict()
            acc = 0
            for i in range(len(self.tree_list) - 1, -1, -1):
                acc += self.tree_list[i]
                self.new_val[self.tree_list[i]] = acc

            del self.tree_list

        root.val = self.new_val[root.val]
        self.convertBST(root.left, False)
        self.convertBST(root.right, False)

        return root


# Runtime: 96 ms, faster than 35.93% of Python3 online submissions for Convert BST to Greater Tree.
# Memory Usage: 16 MB, less than 6.10% of Python3 online submissions for Convert BST to Greater Tree.
