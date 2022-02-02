class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])


# Runtime: 96 ms, faster than 98.07% of Python3 online submissions for Array Partition I.
# Memory Usage: 15.2 MB, less than 5.20% of Python3 online submissions for Array Partition I.
