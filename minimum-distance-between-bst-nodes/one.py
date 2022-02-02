# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def minDiffInBST(self, root: TreeNode, path: List[int] = []) -> int:
        if not root:
            return -1

        vals = []

        min_parent_diff = None
        for parent_val in path:
            diff = abs(parent_val - root.val)
            if min_parent_diff is None or diff < min_parent_diff:
                min_parent_diff = diff

        if min_parent_diff is not None:
            vals.append(min_parent_diff)

        if root.left:
            vals.append(root.val - root.left.val)
            vals.append(self.minDiffInBST(root.left, path + [root.val]))
        if root.right:
            vals.append(root.right.val - root.val)
            vals.append(self.minDiffInBST(root.right, path + [root.val]))

        vals = list(filter(lambda x: x >= 0, vals))

        if not vals:
            return -1

        return min(vals)


# Runtime: 60 ms, faster than 8.96% of Python3 online submissions for Minimum Distance Between BST Nodes.
# Memory Usage: 13.3 MB, less than 6.56% of Python3 online submissions for Minimum Distance Between BST Nodes.
