class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = {0: 1}
        prev_sum = 0
        count = 0

        for val in nums:
            prev_sum += val

            wanted_psum = prev_sum - k
            count += sums.get(wanted_psum, 0)

            sums[prev_sum] = sums.get(prev_sum, 0) + 1

        return count


# Runtime: 553 ms, faster than 5.05% of Python3 online submissions for Subarray Sum Equals K.
# Memory Usage: 16.5 MB, less than 93.61% of Python3 online submissions for Subarray Sum Equals K.
