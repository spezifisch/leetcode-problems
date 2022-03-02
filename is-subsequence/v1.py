class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for char in t:
            if not s:
                break

            if char == s[0]:
                s = s[1:]

        if not s:
            return True

        return False


# Runtime: 47 ms, faster than 51.81% of Python3 online submissions for Is Subsequence.
# Memory Usage: 14 MB, less than 55.23% of Python3 online submissions for Is Subsequence.
