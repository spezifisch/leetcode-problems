class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            num = sum(list(map(int, str(num))))

        return num


# Runtime: 46 ms, faster than 41.75% of Python3 online submissions for Add Digits.
# Memory Usage: 14 MB, less than 81.53% of Python3 online submissions for Add Digits.
