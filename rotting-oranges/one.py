class Solution:
    NEIGHBORS = ((-1, 0), (1, 0), (0, -1), (0, 1))

    def anyFresh(self):
        for row in self.grid:
            for cell in row:
                if cell == 1:
                    return True

        return False

    def hasRottenNeighbor(self, row_idx: int, col_idx: int):
        for offset in self.NEIGHBORS:
            neighbor_row = row_idx + offset[0]
            neighbor_col = col_idx + offset[1]

            if 0 <= neighbor_row < self.rows:
                if 0 <= neighbor_col < self.cols:
                    if self.grid[neighbor_row][neighbor_col] == 2:
                        return True

        return False

    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.grid = grid

        minutes = 0
        while self.anyFresh():
            minutes += 1

            next_grid = [[None] * self.cols for _ in range(self.rows)]
            for row_idx, row in enumerate(self.grid):
                for col_idx, cell in enumerate(row):
                    if cell == 1 and self.hasRottenNeighbor(row_idx, col_idx):
                        cell = 2

                    next_grid[row_idx][col_idx] = cell

            if self.grid == next_grid:
                return -1

            self.grid = next_grid

        return minutes


# Runtime: 48 ms, faster than 86.05% of Python3 online submissions for Rotting Oranges.
# Memory Usage: 13.3 MB, less than 5.12% of Python3 online submissions for Rotting Oranges.
