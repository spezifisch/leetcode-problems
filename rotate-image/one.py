class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for offset in range(n):
            for i in range(n - offset):
                x = offset
                y = offset + i
                swap = matrix[x][y]
                matrix[x][y] = matrix[y][x] 
                matrix[y][x]  = swap
        
            matrix[offset].reverse()
        
# Runtime: 40 ms, faster than 47.74% of Python3 online submissions for Rotate Image.
# Memory Usage: 13.2 MB, less than 5.35% of Python3 online submissions for Rotate Image.

