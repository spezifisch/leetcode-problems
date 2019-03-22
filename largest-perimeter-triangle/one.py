class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A = sorted(A, reverse=True)
        while len(A) >= 3:
            if A[0] < A[1] + A[2]:
                return sum(A[:3])
            A.pop(0)
            
        return 0
    
# Runtime: 92 ms, faster than 20.39% of Python3 online submissions for Largest Perimeter Triangle.
# Memory Usage: 14 MB, less than 5.10% of Python3 online submissions for Largest Perimeter Triangle.

