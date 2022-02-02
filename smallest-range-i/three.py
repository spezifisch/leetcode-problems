class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        diff = max(A) - min(A) - 2 * K
        if diff < 0:
            return 0
        return diff


# Runtime: 44 ms, faster than 68.65% of Python3 online submissions for Smallest Range I.
# Memory Usage: 13.9 MB, less than 8.33% of Python3 online submissions for Smallest Range I.
