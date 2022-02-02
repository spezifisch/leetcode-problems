class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        len_nums = len(nums)
        while i < len_nums:
            if nums[i] >= target:
                return i
            i += 1

        return i


# Runtime: 40 ms, faster than 49.32% of Python3 online submissions for Search Insert Position.
# Memory Usage: 13.7 MB, less than 5.11% of Python3 online submissions for Search Insert Position.
