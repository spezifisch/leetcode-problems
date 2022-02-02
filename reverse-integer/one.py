class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        s = str(x)
        if s[0] == "-":
            s = s[1:]
            neg = True

        s = s[::-1]
        if neg:
            s = "-" + s

        i = int(s)
        if -(2**31) <= i <= 2**31 - 1:
            return i
        return 0


# Runtime: 72 ms, faster than 38.72% of Python3 online submissions for Reverse Integer.
# Memory Usage: 13.4 MB, less than 5.71% of Python3 online submissions for Reverse Integer.
