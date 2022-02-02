class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        val = len(nums)
        for i, num in enumerate(nums):
            val ^= i
            val ^= num

        return val


# Runtime: 68 ms, faster than 25.62% of Python3 online submissions for Missing Number.
# Memory Usage: 14.1 MB, less than 5.25% of Python3 online submissions for Missing Number.
