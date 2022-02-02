class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        possibilities = [[1] for _ in range(n)]
        possibilities[0] = [1] * m

        for i in range(1, n):
            for j in range(1, m):
                possibilities[i].append(
                    possibilities[i - 1][j] + possibilities[i][j - 1]
                )

        return possibilities[-1][-1]


# Runtime: 40 ms, faster than 42.97% of Python3 online submissions for Unique Paths.
# Memory Usage: 13 MB, less than 5.25% of Python3 online submissions for Unique Paths.
