from math import log2, ceil
from itertools import count

class Solution:
    def baseNeg2(self, N: int) -> str:
        if N == 0:
            return "0"
        
        ans = []
        
        max_subtractable = 0
        max_addable = 0
        max_msb_factor = 0
        max_exp = 0
        for exp in count(0, 2):
            msb_factor = 2**exp
            subtractable = max_subtractable + int(2**(exp-1))
            
            if msb_factor - subtractable > N:
                break
                
            max_msb_factor = msb_factor
            max_exp = exp
            max_subtractable = subtractable
            max_addable += msb_factor
        
        acc = max_msb_factor
        subtractable = max_subtractable
        addable = max_addable - max_msb_factor
        ans.append(1)
        for exp in range(max_exp - 1, -1, -1):
            #print("exp", exp, "acc", acc, "subtle", subtractable, "madble", addable)
            if exp % 2 == 1:
                subtractable_without_this = subtractable - 2**exp
                #print("a-s(%d) <= N(%d) < a-swt(%d)?" % (acc - subtractable, N, acc - subtractable_without_this))
                if acc - subtractable <= N < acc - subtractable_without_this:
                    ans.append(1)
                    acc -= 2**exp
                else:
                    ans.append(0)
                
                subtractable = subtractable_without_this
            else:
                previous_deviation = abs(acc - N)
                dev = abs((acc + 2**exp) - N)
                addable_without_this = addable - 2**exp
                max_reachable = acc + addable_without_this
                #print("dev(%d) <= prevdev(%d)? awot(%d)" % (dev, previous_deviation, addable_without_this))
                
                if dev <= previous_deviation or (addable_without_this != 0 and max_reachable < N):
                    ans.append(1)
                    acc += 2**exp
                else:
                    ans.append(0)
                    
                addable = addable_without_this
                
        return "".join(map(str, ans))
    
# Runtime: 40 ms, faster than 32.43% of Python3 online submissions for Convert to Base -2.
# Memory Usage: 13.1 MB, less than 100.00% of Python3 online submissions for Convert to Base -2.

