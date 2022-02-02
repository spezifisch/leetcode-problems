from collections import defaultdict


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        boomerangs = 0

        for idx_i, i in enumerate(points):
            distances = defaultdict(lambda: 0)

            for idx_j, j in enumerate(points):
                if idx_i == idx_j:
                    continue

                distance = (i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2
                distances[distance] += 1
                count = distances[distance]

                if count >= 3:
                    boomerangs -= (count - 2) * (count - 1)

                boomerangs += (count - 1) * count

        return boomerangs


# Runtime: 1424 ms, faster than 43.07% of Python3 online submissions for Number of Boomerangs.
# Memory Usage: 13.4 MB, less than 36.96% of Python3 online submissions for Number of Boomerangs.
