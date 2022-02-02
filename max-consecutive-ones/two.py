class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        ones = 0
        for num in nums:
            if num == 1:
                ones += 1
                if ones > max_ones:
                    max_ones = ones
            else:
                ones = 0

        return max_ones


# Runtime: 76 ms, faster than 72.81% of Python3 online submissions for Max Consecutive Ones.
# Memory Usage: 13.4 MB, less than 6.50% of Python3 online submissions for Max Consecutive Ones.
