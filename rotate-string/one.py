from collections import deque

class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if A == B:
            return True
        if not A or not B:
            return False
        
        A = deque(A)
        B = deque(B)
        for _ in range(len(A) - 1):
            A.rotate(-1)
            if A == B:
                return True
            
        return False
        
# Runtime: 36 ms, faster than 74.97% of Python3 online submissions for Rotate String.
# Memory Usage: 13.2 MB, less than 6.15% of Python3 online submissions for Rotate String.

