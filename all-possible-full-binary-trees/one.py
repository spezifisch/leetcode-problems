# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        self.cache = dict()

    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N % 2 == 0:
            return []
        if N == 1:
            return [TreeNode(0)]

        trees = []

        for left_children in range(1, N - 2 + 1, 2):
            # subtract 1 for the root node
            right_children = N - 1 - left_children

            if left_children in self.cache:
                left = self.cache[left_children]
            else:
                left = self.allPossibleFBT(left_children)
                self.cache[left_children] = left

            if right_children in self.cache:
                right = self.cache[right_children]
            else:
                right = self.allPossibleFBT(right_children)
                self.cache[right_children] = right

            for l in left:
                for r in right:
                    tree = TreeNode(0)
                    tree.left = l
                    tree.right = r
                    trees.append(tree)

        return trees


# Runtime: 168 ms, faster than 77.58% of Python3 online submissions for All Possible Full Binary Trees.
# Memory Usage: 16.1 MB, less than 33.90% of Python3 online submissions for All Possible Full Binary Trees.
