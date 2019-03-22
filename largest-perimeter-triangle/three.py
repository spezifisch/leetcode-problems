class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A = sorted(A, reverse=True)
        for i in range(len(A) - 2):
            d = A[i+1] + A[i+2]
            if A[i] < d:
                return A[i] + d
            
        return 0
    
# Runtime: 72 ms, faster than 98.16% of Python3 online submissions for Largest Perimeter Triangle.
# Memory Usage: 13.8 MB, less than 5.10% of Python3 online submissions for Largest Perimeter Triangle.

