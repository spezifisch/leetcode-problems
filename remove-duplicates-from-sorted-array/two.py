class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        len_nums = len(nums)
        i = 0
        previous = None
        while i < len_nums:
            val = nums[i]
            if previous is None:
                i += 1
            else:
                if previous == val:
                    # remove dup
                    del nums[i]
                    len_nums -= 1
                else:
                    i += 1
            
            previous = val
            
        return len_nums
    
# Runtime: 80 ms, faster than 43.17% of Python3 online submissions for Remove Duplicates from Sorted Array.
# Memory Usage: 14.8 MB, less than 5.43% of Python3 online submissions for Remove Duplicates from Sorted Array.

