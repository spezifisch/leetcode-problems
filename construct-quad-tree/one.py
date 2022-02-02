"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


class Solution:
    def construct(self, grid: List[List[int]]) -> "Node":
        if not grid:
            return None

        N = len(grid)
        leaf_val = grid[0][0]
        is_leaf = True
        for row in grid:
            for cell in row:
                if leaf_val != cell:
                    is_leaf = False
                    break

            if not is_leaf:
                break

        if N == 1 or is_leaf:
            return Node(leaf_val, True, None, None, None, None)

        Nhalf = N // 2
        grid_tl = [row[:Nhalf] for row in grid[:Nhalf]]
        grid_tr = [row[Nhalf:] for row in grid[:Nhalf]]
        grid_bl = [row[:Nhalf] for row in grid[Nhalf:]]
        grid_br = [row[Nhalf:] for row in grid[Nhalf:]]

        node_tl = self.construct(grid_tl)
        node_tr = self.construct(grid_tr)
        node_bl = self.construct(grid_bl)
        node_br = self.construct(grid_br)

        return Node("*", False, node_tl, node_tr, node_bl, node_br)


# Runtime: 96 ms, faster than 89.55% of Python3 online submissions for Construct Quad Tree.
# Memory Usage: 15.1 MB, less than 5.45% of Python3 online submissions for Construct Quad Tree.
