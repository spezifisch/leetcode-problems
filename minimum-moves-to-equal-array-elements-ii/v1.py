import statistics


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        med = round(statistics.median(nums))
        return sum([abs(num - med) for num in nums])


# Runtime: 85 ms, faster than 85.41% of Python3 online submissions for Minimum Moves to Equal Array Elements II.
# Memory Usage: 15.3 MB, less than 95.33% of Python3 online submissions for Minimum Moves to Equal Array Elements II.
