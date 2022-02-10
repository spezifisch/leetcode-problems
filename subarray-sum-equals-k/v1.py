class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = {0: 1}
        prev_sum = 0
        psum = [0] * (len(nums) + 1)
        count = 0

        for i, val in enumerate(nums):
            prev_sum += val
            psum[i + 1] = prev_sum

            wanted_psum = prev_sum - k
            if wanted_psum in sums:
                count += sums.get(wanted_psum, 0)

            sums[prev_sum] = sums.get(prev_sum, 0) + 1

        # print("--", k, nums)
        # print(psum)
        # print(sums)
        return count


# Runtime: 536 ms, faster than 6.06% of Python3 online submissions for Subarray Sum Equals K.
# Memory Usage: 16.6 MB, less than 93.61% of Python3 online submissions for Subarray Sum Equals K.
