class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums = []
        for num in nums1:
            idx = nums2.index(num)
            insert_num = -1
            for bigger_num in nums2[idx + 1:]:
                if bigger_num > num:
                    insert_num = bigger_num
                    break
                    
            nums.append(insert_num)
            
        return nums
            
# Runtime: 84 ms, faster than 20.69% of Python3 online submissions for Next Greater Element I.
# Memory Usage: 13.4 MB, less than 5.26% of Python3 online submissions for Next Greater Element I.

