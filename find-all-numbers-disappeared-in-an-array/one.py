class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return list(set(nums) ^ set(range(1, len(nums) + 1)))


# Runtime: 168 ms, faster than 62.36% of Python3 online submissions for Find All Numbers Disappeared in an Array.
# Memory Usage: 24.9 MB, less than 5.39% of Python3 online submissions for Find All Numbers Disappeared in an Array.
