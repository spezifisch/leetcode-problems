from typing import Tuple

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
        
    def explore(self, pos: Tuple[int, int], path: List[int]) -> None:
        if pos == self.goal:
            if len(path) == self.target_path_len:
                self.possibilities += 1
                
            return
        
        all_neighbors = [
            [pos[0] - 1, pos[1]],
            [pos[0] + 1, pos[1]],
            [pos[0], pos[1] - 1],
            [pos[0], pos[1] + 1],
        ]
        
        for neighbor in all_neighbors:
            if not (0 <= neighbor[0] < self.rows):
                continue
            if not (0 <= neighbor[1] < self.cols):
                continue
            if neighbor in path:
                continue
            if neighbor in self.obstacles:
                continue
            
            self.explore(neighbor, [neighbor] + path)

# Runtime: 72 ms, faster than 55.96% of Python3 online submissions for Unique Paths III.
# Memory Usage: 13.3 MB, less than 10.42% of Python3 online submissions for Unique Paths III.

