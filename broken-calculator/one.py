class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        if X >= Y:
            return X - Y

        ops = 0
        while X != Y:
            ops += 1

            if X < Y:
                if Y % 2 == 1:
                    Y += 1
                else:
                    Y //= 2
            else:
                Y += 1

        return ops


# Runtime: 1792 ms, faster than 6.04% of Python3 online submissions for Broken Calculator.
# Memory Usage: 13.3 MB, less than 5.77% of Python3 online submissions for Broken Calculator.
