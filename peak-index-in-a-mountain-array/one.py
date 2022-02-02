class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        max_idx = None
        max_value = -1
        for i, elem in enumerate(A):
            if elem > max_value:
                max_value = elem
                max_idx = i

        return max_idx


# Runtime: 44 ms, faster than 39.84% of Python3 online submissions for Peak Index in a Mountain Array.
# Memory Usage: 14.4 MB, less than 5.42% of Python3 online submissions for Peak Index in a Mountain Array.
