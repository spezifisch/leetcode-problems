class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        possibilities = [[0]*m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                if not i or not j:
                    possibilities[i][j] = 1
                else:
                    possibilities[i][j] = possibilities[i - 1][j] + possibilities[i][j - 1]
                    
        return possibilities[-1][-1]

# Runtime: 52 ms, faster than 18.66% of Python3 online submissions for Unique Paths.
# Memory Usage: 13 MB, less than 5.25% of Python3 online submissions for Unique Paths.

