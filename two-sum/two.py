class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for a_idx, a_value in enumerate(nums):
            # start looking for the second value after the current value
            offset = a_idx + 1
            
            wanted = target - a_value
            if wanted in nums[offset:]:
                return [a_idx, offset+nums[offset:].index(wanted)]
                
# Accepted	928 ms	13.6 MB	python3

