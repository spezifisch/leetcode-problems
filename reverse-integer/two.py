class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        s = s[::-1]
        if s[-1] == "-":
            s = "-" + s[:-1]

        i = int(s)
        if -(2**31) <= i <= 2**31 - 1:
            return i
        return 0


# Runtime: 68 ms, faster than 41.81% of Python3 online submissions for Reverse Integer.
# Memory Usage: 13.3 MB, less than 5.71% of Python3 online submissions for Reverse Integer.
