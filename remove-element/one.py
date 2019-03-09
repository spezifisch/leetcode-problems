class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val:
                del nums[i]
            else:
                i += 1
                
        return len(nums)
        
# Runtime: 40 ms, faster than 57.05% of Python3 online submissions for Remove Element.
# Memory Usage: 13.1 MB, less than 5.09% of Python3 online submissions for Remove Element.

