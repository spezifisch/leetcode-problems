class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        return sorted(points, key=lambda point: point[0] ** 2 + point[1] ** 2)[:K]


# Runtime: 348 ms, faster than 81.22% of Python3 online submissions for K Closest Points to Origin.
# Memory Usage: 16.9 MB, less than 30.39% of Python3 online submissions for K Closest Points to Origin.
