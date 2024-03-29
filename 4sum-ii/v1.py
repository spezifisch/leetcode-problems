class Solution:
    def fourSumCount(
        self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]
    ) -> int:
        count = 0
        sums12 = {}
        for a in nums1:
            for b in nums2:
                s = a + b
                sums12[s] = sums12.get(s, 0) + 1

        for a in nums3:
            for b in nums4:
                s = a + b
                count += sums12.get(-s, 0)

        return count


# Runtime: 741 ms, faster than 82.16% of Python3 online submissions for 4Sum II.
# Memory Usage: 14.1 MB, less than 99.75% of Python3 online submissions for 4Sum II.
