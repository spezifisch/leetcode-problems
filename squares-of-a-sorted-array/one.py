class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        nums = map(lambda x: x**2, A)
        return sorted(nums)
    
# Runtime: 200 ms, faster than 21.98% of Python3 online submissions for Squares of a Sorted Array.
# Memory Usage: 15 MB, less than 5.22% of Python3 online submissions for Squares of a Sorted Array.

