class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        N = len(grid)
        area = 0

        for x in range(N):
            for y in range(N):
                height = grid[y][x]
                if height == 0:
                    continue

                area += 2 + height * 4
                for neighbor in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    nx = x + neighbor[0]
                    ny = y + neighbor[1]
                    if not (0 <= nx < N and 0 <= ny < N):
                        continue

                    neighbor_height = grid[ny][nx]
                    if neighbor_height > 0:
                        area -= min(neighbor_height, height)

        return area


# Runtime: 88 ms, faster than 36.64% of Python3 online submissions for Surface Area of 3D Shapes.
# Memory Usage: 13.3 MB, less than 8.70% of Python3 online submissions for Surface Area of 3D Shapes.
