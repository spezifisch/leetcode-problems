class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])


# Runtime: 92 ms, faster than 99.83% of Python3 online submissions for Array Partition I.
# Memory Usage: 14.9 MB, less than 5.20% of Python3 online submissions for Array Partition I.
