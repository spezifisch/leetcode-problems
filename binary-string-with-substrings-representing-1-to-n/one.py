class Solution:
    def queryString(self, S: str, N: int) -> bool:
        for n in range(1, N + 1):
            binn = bin(n)[2:]
            if not binn in S:
                return False

        return True


# Runtime: 36 ms, faster than 100.00% of Python3 online submissions for Binary String With Substrings Representing 1 To N.
# Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Binary String With Substrings Representing 1 To N.
