class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        if len(A) <= 1:
            return 0
        
        amax = max(A)
        amin = min(A)
        
        diff = amax - amin
        return max(0, diff - 2 * K)
    
# Runtime: 48 ms, faster than 45.58% of Python3 online submissions for Smallest Range I.
# Memory Usage: 14.1 MB, less than 8.33% of Python3 online submissions for Smallest Range I.

