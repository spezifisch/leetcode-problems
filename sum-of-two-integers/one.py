class Solution:
    def getSum(self, a: int, b: int) -> int:
        pos = []
        neg = []
        
        if a > 0:
            pos = [None] * a
        elif a < 0:
            neg = [None] * a
            
        if b > 0:
            if pos:
                pos.extend([None] * b)
            elif neg:
                for _ in range(b):
                    if neg:
                        neg.pop()
                    else:
                        pos.push(None)
        elif b < 0:
            if neg:
                neg.extend([None] * b)
            elif pos:
                for _ in range(b):
                    if pos:
                        pos.pop()
                    else:
                        neg.push(None)
                        
        if neg:
            return -1 * len(neg)
        
        return len(pos)
    
# MemoryError
# Line 7 in getSum (Solution.py)
# Line 44 in __helper__ (Solution.py)
# Line 60 in _driver (Solution.py)
# Line 71 in <module> (Solution.py)
#
# Last executed input
# 2147483647
# -2147483648
 
