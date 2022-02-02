class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        ops = 0
        while X < Y:
            ops += 1
            
            if Y % 2 == 1:
                Y += 1
            else:
                Y //= 2

        return ops + X - Y

# Runtime: 36 ms, faster than 57.58% of Python3 online submissions for Broken Calculator.
# Memory Usage: 13.3 MB, less than 5.77% of Python3 online submissions for Broken Calculator.

