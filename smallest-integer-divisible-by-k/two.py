class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if (K % 2) == 0:
            return -1
        if (K % 5) == 0:
            return -1
        
        num = 1
        i = 0
        while True:
            if (num % K) == 0:
                return i + 1
            
            num = num * 10 + 1
            i += 1
            
        return -1

# Runtime: 1980 ms, faster than 100.00% of Python3 online submissions for Smallest Integer Divisible by K.
# Memory Usage: 13.4 MB, less than 100.00% of Python3 online submissions for Smallest Integer Divisible by K.

