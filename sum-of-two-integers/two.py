from math import log2

class Solution:
    def getSum(self, a: int, b: int) -> int:
        return int(log2(2**a * 2**b))
    
# Time Limit Exceeded
#
# Last executed input
# 2147483647
# -2147483648

