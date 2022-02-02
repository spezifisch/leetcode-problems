class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        if not n:
            return
        m = len(obstacleGrid[0])
        if not m:
            return

        # initialize top and left border values
        possibilities = [[1] for _ in range(n)]
        possibilities[0] = [1] * m

        # an obstacle in the top row blocks the remaining possibilities in the row (set to 0).
        if 1 in obstacleGrid[0]:
            border_obstacle_idx = obstacleGrid[0].index(1)
            possibilities[0][border_obstacle_idx:] = [0] * (m - border_obstacle_idx)

        # same with an obstacle in the left column. set remaining cols to 0 because we can't get there.
        reachable = True
        for i in range(n):
            if obstacleGrid[i][0] == 1:
                reachable = False

            if not reachable:
                possibilities[i][0] = 0

        # calculate number of possibilities to reach fields
        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j] == 0:
                    # free space
                    possibilities[i].append(
                        possibilities[i - 1][j] + possibilities[i][j - 1]
                    )
                else:
                    # obstacle => impossible to reach
                    possibilities[i].append(0)

        return possibilities[-1][-1]


# Runtime: 40 ms, faster than 60.20% of Python3 online submissions for Unique Paths II.
# Memory Usage: 13.1 MB, less than 5.19% of Python3 online submissions for Unique Paths II.
