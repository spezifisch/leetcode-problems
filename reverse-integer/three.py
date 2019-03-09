class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        s = s[::-1]
        if s[-1] == "-":
            s = "-" + s[:-1]
            
        i = int(s)
        mint = 2**31
        if -mint <= i <= mint-1:
            return i
        return 0
    
# Runtime: 56 ms, faster than 60.66% of Python3 online submissions for Reverse Integer.
# Memory Usage: 13.2 MB, less than 5.71% of Python3 online submissions for Reverse Integer.

