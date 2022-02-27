# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs_left(
        self, *, level: int, node: Optional[TreeNode], left_distance: int
    ) -> None:
        if not node:
            return

        if level not in self.leftmost_node:
            node.left_distance = left_distance
            self.leftmost_node[level] = node

        left_distance *= 2
        self.dfs_left(level=level + 1, node=node.left, left_distance=left_distance)
        self.dfs_left(level=level + 1, node=node.right, left_distance=left_distance + 1)

    def dfs_right(
        self, *, level: int, node: Optional[TreeNode], right_distance: int
    ) -> None:
        if not node:
            return

        if level not in self.rightmost_node:
            node.right_distance = right_distance
            self.rightmost_node[level] = node

        right_distance *= 2
        self.dfs_right(level=level + 1, node=node.right, right_distance=right_distance)
        self.dfs_right(
            level=level + 1, node=node.left, right_distance=right_distance + 1
        )

    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.leftmost_node = {}
        self.rightmost_node = {}

        self.dfs_left(level=0, node=root, left_distance=0)
        self.dfs_right(level=0, node=root, right_distance=0)

        max_width = 1
        for level in range(min(len(self.leftmost_node), len(self.rightmost_node))):
            lm = self.leftmost_node[level]
            rm = self.rightmost_node[level]

            width = 2**level - lm.left_distance - rm.right_distance
            max_width = max(max_width, width)

        # l = 6
        # print("lmnodes", self.leftmost_node.keys())
        # print("rmnodes", self.rightmost_node.keys())
        # print(f"full node level would be {2**l}")
        # print(f"leftmost.dist_left {self.leftmost_node[l].left_distance}")
        # print(f"rightmost.dist_right {self.rightmost_node[l].right_distance}")

        return max_width


# Runtime: 71 ms, faster than 39.65% of Python3 online submissions for Maximum Width of Binary Tree.
# Memory Usage: 20.6 MB, less than 5.77% of Python3 online submissions for Maximum Width of Binary Tree.
