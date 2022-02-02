from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []

        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1

        # nums1 is the bigger one
        nums1_counter = Counter(nums1)
        nums2_counter = Counter(nums2)

        result = []
        for num, cnt2 in nums2_counter.items():
            cnt1 = nums1_counter[num]
            cnt = min(cnt1, cnt2)

            if cnt:
                result += [num] * cnt

        return result


# Runtime: 40 ms, faster than 86.62% of Python3 online submissions for Intersection of Two Arrays II.
# Memory Usage: 13.3 MB, less than 5.81% of Python3 online submissions for Intersection of Two Arrays II.
