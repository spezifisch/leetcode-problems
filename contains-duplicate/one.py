class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


# Runtime: 44 ms, faster than 91.53% of Python3 online submissions for Contains Duplicate.
# Memory Usage: 18.8 MB, less than 25.52% of Python3 online submissions for Contains Duplicate.
