class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        if len(A) <= 1:
            return 0
        
        A.sort()
        amax = A[-1]
        amin = A[0]
        
        diff = amax - amin
        return max(0, diff - 2 * K)
    
# Runtime: 60 ms, faster than 27.88% of Python3 online submissions for Smallest Range I.
# Memory Usage: 14 MB, less than 8.33% of Python3 online submissions for Smallest Range I.

