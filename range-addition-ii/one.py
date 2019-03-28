class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m * n
        x = min(ops, key=lambda a: a[0])[0]
        y = min(ops, key=lambda a: a[1])[1]
        return x * y

# Runtime: 40 ms, faster than 80.26% of Python3 online submissions for Range Addition II.
# Memory Usage: 14 MB, less than 20.83% of Python3 online submissions for Range Addition II.

