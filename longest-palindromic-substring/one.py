class Solution:
    @staticmethod
    def expand_palindrome(s, a, b):
        if a >= 0 and b < len(s):
            if s[a] == s[b]:
                deeper = Solution.expand_palindrome(s, a - 1, b + 1)
                if deeper:
                    return deeper
                else:
                    return (a, b)

        return

    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        longest = ""

        for i in range(len(s)):
            ab = self.expand_palindrome(s, i, i)
            if ab:
                a, b = ab
                asym_len = b - a + 1
                if asym_len > max_len:
                    max_len = asym_len
                    longest = s[a : b + 1]

            ab = self.expand_palindrome(s, i, i + 1)
            if ab:
                a, b = ab
                sym_len = b - a + 1
                if sym_len > max_len:
                    max_len = sym_len
                    longest = s[a : b + 1]

        return longest


# Runtime: 1668 ms, faster than 48.33% of Python3 online submissions for Longest Palindromic Substring.
# Memory Usage: 13.3 MB, less than 24.59% of Python3 online submissions for Longest Palindromic Substring.
