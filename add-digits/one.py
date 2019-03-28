class Solution:
    def addDigits(self, num: int) -> int:
        num_str = str(num)
        
        while len(num_str) > 1:
            num_sum = sum([int(c) for c in num_str])
            num_str = str(num_sum)
        
        return int(num_str)
    
# Runtime: 60 ms, faster than 29.73% of Python3 online submissions for Add Digits.
# Memory Usage: 13.2 MB, less than 5.82% of Python3 online submissions for Add Digits.

