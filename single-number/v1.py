class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ret = 0
        for num in nums:
            ret ^= num

        return ret


# Runtime: 238 ms, faster than 29.31% of Python3 online submissions for Single Number.
# Memory Usage: 16.7 MB, less than 30.94% of Python3 online submissions for Single Number.
