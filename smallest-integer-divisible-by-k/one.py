class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if (K % 2) == 0:
            return -1
        if (K % 5) == 0:
            return -1
        
        num = 1
        while True:
            if (num % K) == 0:
                return len(str(num))
            
            num = num * 10 + 1
            
        return -1
    
# Runtime: 2016 ms, faster than 100.00% of Python3 online submissions for Smallest Integer Divisible by K.
# Memory Usage: 13.3 MB, less than 100.00% of Python3 online submissions for Smallest Integer Divisible by K.

