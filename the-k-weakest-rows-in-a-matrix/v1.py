class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return [x[0] for x in sorted(enumerate(mat), key=lambda m: sum(m[1]))[:k]]


# Runtime: 108 ms, faster than 96.70% of Python3 online submissions for The K Weakest Rows in a Matrix.
# Memory Usage: 14.3 MB, less than 55.07% of Python3 online submissions for The K Weakest Rows in a Matrix.
