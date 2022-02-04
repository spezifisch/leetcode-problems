class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_len = 0
        for i_start in range(len(nums)):
            for j_len in range(0, len(nums) - i_start + 1, 2):
                chunk = nums[i_start : i_start + j_len]
                if sum(chunk) == j_len / 2:
                    max_len = max(max_len, j_len)

        return max_len


# Time Limit Exceeded
