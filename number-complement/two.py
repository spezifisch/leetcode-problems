class Solution:
    @staticmethod
    def findMSB(num: int) -> int:
        for i in range(31, -1, -1):
            if num & (1<<i) != 0:
                return i
    
    @staticmethod
    def getMask(msb: int) -> int:
        mask = 0
        for i in range(msb + 1):
            mask |= (1<<i)
            
        return mask
    
    def findComplement(self, num: int) -> int:
        msb = self.findMSB(num)
        mask = self.getMask(msb)
        return num ^ mask
    
# Runtime: 40 ms, faster than 54.98% of Python3 online submissions for Number Complement.
# Memory Usage: 13 MB, less than 5.55% of Python3 online submissions for Number Complement.

