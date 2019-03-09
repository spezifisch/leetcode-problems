class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nl = len(nums)
        i = 0
        while i < nl:
            if nums[i] == val:
                del nums[i]
                nl -= 1
            else:
                i += 1
                
        return nl
        
# Runtime: 40 ms, faster than 57.05% of Python3 online submissions for Remove Element.
# Memory Usage: 13.3 MB, less than 5.09% of Python3 online submissions for Remove Element.

