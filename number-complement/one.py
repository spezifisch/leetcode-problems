class Solution:
    def findComplement(self, num: int) -> int:
        b = bin(num)[2:]
        b = b.replace("0", "_").replace("1", "0").replace("_", "1")
        return int(b, 2)
    
# Runtime: 44 ms, faster than 32.81% of Python3 online submissions for Number Complement.
# Memory Usage: 13.2 MB, less than 5.55% of Python3 online submissions for Number Complement.

