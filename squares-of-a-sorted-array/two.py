class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        nums = [x**2 for x in A]
        return sorted(nums)


# Runtime: 200 ms, faster than 21.98% of Python3 online submissions for Squares of a Sorted Array.
# Memory Usage: 15.1 MB, less than 5.22% of Python3 online submissions for Squares of a Sorted Array.
