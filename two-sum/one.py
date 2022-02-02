class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for a_idx, a_value in enumerate(nums):
            # start looking for the second value after the current value
            offset = a_idx + 1
            for b_idx, b_value in enumerate(nums[offset:]):
                # the first element (b_idx=0) is actually at `offset`
                b_idx += offset
                if nums[a_idx] + nums[b_idx] == target:
                    return [a_idx, b_idx]


# Runtime: 8924 ms, faster than 5.01% of Python3 online submissions for Two Sum.
# Memory Usage: 13.7 MB, less than 33.49% of Python3 online submissions for Two Sum.
