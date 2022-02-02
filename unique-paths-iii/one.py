from typing import Tuple
from operator import add


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        if not len(grid) or not len(grid[0]):
            return 0

        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])

        self.obstacles = []
        self.start = None
        self.goal = None

        for row_idx, row in enumerate(grid):
            for col_idx, elem in enumerate(row):
                coord = [row_idx, col_idx]
                if elem == 1:
                    self.start = coord
                elif elem == 2:
                    self.goal = coord
                elif elem == -1:
                    self.obstacles.append(coord)
                elif elem == 0:
                    pass
                else:
                    raise ValueError("unknown element")

        if not self.start or not self.goal:
            raise ValueError("start or end missing")

        self.target_path_len = self.rows * self.cols - len(self.obstacles)
        self.possibilities = 0

        self.explore(self.start, [self.start])

        return self.possibilities

    @staticmethod
    def add_elements(a, b):
        return list(map(add, a, b))

    def is_valid_element(self, elem: Tuple[int, int]) -> bool:
        if elem in self.obstacles:
            return False
        if not (0 <= elem[0] < self.rows):
            return False
        if not (0 <= elem[1] < self.cols):
            return False
        return True

    def explore(self, pos: Tuple[int, int], path: List[int]):
        neighbors = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        neighbors = [self.add_elements(neighbor, pos) for neighbor in neighbors]
        neighbors = list(
            filter(
                lambda elem: elem not in path and self.is_valid_element(elem), neighbors
            )
        )
        # print("explore", pos, "path", path, "neighbors", neighbors)

        if not len(neighbors):
            if pos == self.goal and len(path) == self.target_path_len:
                self.possibilities += 1

            return

        for neighbor in neighbors:
            self.explore(neighbor, path + [neighbor])


# Runtime: 268 ms, faster than 5.13% of Python3 online submissions for Unique Paths III.
# Memory Usage: 12.9 MB, less than 12.50% of Python3 online submissions for Unique Paths III.
