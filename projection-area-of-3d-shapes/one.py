class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        xy_plane = 0
        xz_plane = 0
        yz_plane = 0
        dim = len(grid)
        
        x_highest = [0]*dim
        y_highest = [0]*dim
        
        for i in range(dim):
            for j in range(dim):
                v = grid[i][j]
                if v > 0:
                    xy_plane += 1
                
                    if v > x_highest[i]:
                        x_highest[i] = v
                    if v > y_highest[j]:
                        y_highest[j] = v
                        
        xz_plane = sum(x_highest)
        yz_plane = sum(y_highest)
        
        return xy_plane + xz_plane + yz_plane
    
# Runtime: 44 ms, faster than 73.05% of Python3 online submissions for Projection Area of 3D Shapes.
# Memory Usage: 13.2 MB, less than 7.84% of Python3 online submissions for Projection Area of 3D Shapes.

