class Solution:
    @staticmethod
    def isSelfDividing(val):
        for digit_c in str(val):
            digit = int(digit_c)
            if digit == 0:
                return False
            if val % digit != 0:
                return False
            
        return True
    
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ret = []
        for i in range(left, right + 1):
            if Solution.isSelfDividing(i):
                ret.append(i)
                
        return ret
    
# Runtime: 60 ms, faster than 70.83% of Python3 online submissions for Self Dividing Numbers.
# Memory Usage: 13.2 MB, less than 6.29% of Python3 online submissions for Self Dividing Numbers.

