class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        skyline_left = [max(row) for row in grid]
        dim = len(grid)
        rot_grid = [[grid[j][i] for j in range(dim)] for i in range(dim)]
        skyline_top = [max(col) for col in rot_grid]

        raises = 0
        for row_id in range(dim):
            for col_id in range(dim):
                max_height = min(skyline_left[row_id], skyline_top[col_id])
                may_add = max_height - grid[row_id][col_id]
                raises += may_add

        return raises


# Runtime: 64 ms, faster than 34.43% of Python3 online submissions for Max Increase to Keep City Skyline.
# Memory Usage: 13.3 MB, less than 5.55% of Python3 online submissions for Max Increase to Keep City Skyline.
