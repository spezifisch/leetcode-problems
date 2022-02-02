# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        self.levels = []
        self.buildLevelOrder(root, depth=0)

        return [sum(level) / len(level) for level in self.levels]

    def buildLevelOrder(self, root: TreeNode, depth: int) -> None:
        if not root:
            return None

        if depth >= len(self.levels):
            self.levels.append([root.val])
        else:
            self.levels[depth].append(root.val)

        self.buildLevelOrder(root.left, depth + 1)
        self.buildLevelOrder(root.right, depth + 1)


# Runtime: 68 ms, faster than 34.31% of Python3 online submissions for Average of Levels in Binary Tree.
# Memory Usage: 16.2 MB, less than 5.38% of Python3 online submissions for Average of Levels in Binary Tree.
