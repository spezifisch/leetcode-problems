class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_len = 0
        for i_start in range(len(nums)):
            sum_chunk = 0
            for j_len in range(2, len(nums) - i_start + 1, 2):
                part = nums[i_start + j_len - 2 : i_start + j_len]
                sum_chunk += sum(part)
                if sum_chunk == j_len / 2:
                    max_len = max(max_len, j_len)

        return max_len


# Time Limit Exceeded
