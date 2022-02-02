class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return max(map(len, "".join(map(str, nums)).split("0")))


# Runtime: 88 ms, faster than 60.18% of Python3 online submissions for Max Consecutive Ones.
# Memory Usage: 13.7 MB, less than 6.50% of Python3 online submissions for Max Consecutive Ones.
