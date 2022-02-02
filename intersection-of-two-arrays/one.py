class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))


# Runtime: 56 ms, faster than 32.17% of Python3 online submissions for Intersection of Two Arrays.
# Memory Usage: 13.1 MB, less than 5.34% of Python3 online submissions for Intersection of Two Arrays.
