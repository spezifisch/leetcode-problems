# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        if not root:
            return ""

        smallest = None
        ordA = ord("a")
        stack = [(root, "")]
        while len(stack):
            node, path = stack.pop()
            char = chr(ordA + node.val)
            path = char + path

            if not node.left and not node.right:
                if smallest is None or path < smallest:
                    smallest = path
            else:
                if node.left:
                    stack.append((node.left, path))
                if node.right:
                    stack.append((node.right, path))

        return smallest


# Runtime: 52 ms, faster than 30.74% of Python3 online submissions for Smallest String Starting From Leaf.
# Memory Usage: 14.7 MB, less than 6.10% of Python3 online submissions for Smallest String Starting From Leaf.
