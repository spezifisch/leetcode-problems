from collections import defaultdict

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        counts = defaultdict(lambda: 0)
        for num in nums:
            counts[num] += 1
            
        max_values = None
        max_count = 0
        for value, count in counts.items():
            if max_values is None or count > max_count:
                max_count = count
                max_values = [value]
            elif count == max_count:
                max_values.append(value)
                    
        sub_lens = []
        for value in max_values:
            start = nums.index(value)
            end = len(nums) - 1 - nums[::-1].index(value)
            sub_lens.append(1 + end - start)
            
        return min(sub_lens)
    
# Runtime: 664 ms, faster than 15.27% of Python3 online submissions for Degree of an Array.
# Memory Usage: 14.4 MB, less than 14.06% of Python3 online submissions for Degree of an Array.

