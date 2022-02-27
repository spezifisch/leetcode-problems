# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(
        self,
        *,
        level: int,
        node: Optional[TreeNode],
        left_distance: int,
        right_distance: int
    ) -> None:
        if not node:
            return

        node.left_distance = left_distance
        node.right_distance = right_distance

        if level not in self.leftmost_node:
            self.leftmost_node[level] = node

        self.rightmost_node[level] = node

        left_distance *= 2
        right_distance *= 2
        self.dfs(
            level=level + 1,
            node=node.left,
            left_distance=left_distance,
            right_distance=right_distance + 1,
        )
        self.dfs(
            level=level + 1,
            node=node.right,
            left_distance=left_distance + 1,
            right_distance=right_distance,
        )

    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.leftmost_node = {}
        self.rightmost_node = {}

        self.dfs(level=0, node=root, left_distance=0, right_distance=0)

        max_width = 1
        for level in range(min(len(self.leftmost_node), len(self.rightmost_node))):
            lm = self.leftmost_node[level]
            rm = self.rightmost_node[level]

            width = 2**level - lm.left_distance - rm.right_distance
            max_width = max(max_width, width)

        return max_width


# Runtime: 65 ms, faster than 50.09% of Python3 online submissions for Maximum Width of Binary Tree.
# Memory Usage: 20.1 MB, less than 5.77% of Python3 online submissions for Maximum Width of Binary Tree.
