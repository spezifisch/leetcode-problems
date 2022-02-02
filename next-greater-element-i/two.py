class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2_indices = dict()
        for i, num in enumerate(nums2):
            nums2_indices[num] = i

        nums = []
        for num in nums1:
            idx = nums2_indices[num]
            insert_num = -1
            for bigger_num in nums2[idx + 1 :]:
                if bigger_num > num:
                    insert_num = bigger_num
                    break

            nums.append(insert_num)

        return nums


# Runtime: 56 ms, faster than 49.56% of Python3 online submissions for Next Greater Element I.
# Memory Usage: 13 MB, less than 5.26% of Python3 online submissions for Next Greater Element I.
