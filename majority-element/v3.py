class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[int(len(nums) / 2)]


# Runtime: 256 ms, faster than 37.70% of Python3 online submissions for Majority Element.
# Memory Usage: 15.5 MB, less than 43.74% of Python3 online submissions for Majority Element.
