class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        rows = len(M)
        cols = len(M[0])
        out = [[None] * cols for _ in range(rows)]
        
        offsets = (-1, 0, 1)
        
        for row in range(rows):
            for col in range(cols):
                neighbors = 0
                neighbors_sum = 0
                for ni in offsets:
                    for nj in offsets:
                        neighbor_row = row + ni
                        neighbor_col = col + nj
                        if not (0 <= neighbor_row < rows):
                            continue
                        if not (0 <= neighbor_col < cols):
                            continue

                        neighbors += 1
                        neighbors_sum += M[neighbor_row][neighbor_col]

                out[row][col] = neighbors_sum // neighbors
                
        return out
    
# Runtime: 544 ms, faster than 71.77% of Python3 online submissions for Image Smoother.
# Memory Usage: 13.6 MB, less than 8.33% of Python3 online submissions for Image Smoother.

