class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return 1 + (num - 1) % 9
    
# Runtime: 56 ms, faster than 64.66% of Python3 online submissions for Add Digits.
# Memory Usage: 12.9 MB, less than 5.82% of Python3 online submissions for Add Digits.

