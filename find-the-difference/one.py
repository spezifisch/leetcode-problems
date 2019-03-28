class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        t = list(t)
        for c in s:
            t.remove(c)
            
        return t[0]
    
# Runtime: 64 ms, faster than 11.61% of Python3 online submissions for Find the Difference.
# Memory Usage: 13.1 MB, less than 5.00% of Python3 online submissions for Find the Difference.

