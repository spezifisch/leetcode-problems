from collections import defaultdict
from math import ceil

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = defaultdict(lambda: 0)
        wanted_count = ceil(len(nums) / 2)
        for num in nums:
            counts[num] += 1
            if counts[num] >= wanted_count:
                return num
            
        assert(False)
        
# Runtime: 56 ms, faster than 55.22% of Python3 online submissions for Majority Element.
# Memory Usage: 14.2 MB, less than 5.18% of Python3 online submissions for Majority Element.

