class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sum_map = {}
        csum = 0
        max_len = 0

        for i in range(len(nums)):
            val = nums[i] * 2 - 1
            csum += val

            if csum == 0:
                max_len = i + 1

            if csum in sum_map:
                chunk_len = i - sum_map[csum]
                max_len = max(max_len, chunk_len)
            else:
                sum_map[csum] = i

        return max_len


# Runtime: 1148 ms, faster than 40.35% of Python3 online submissions for Contiguous Array.
# Memory Usage: 19.4 MB, less than 21.71% of Python3 online submissions for Contiguous Array.
