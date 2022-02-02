from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        palindrome_len = 0
        got_odd = False
        for c_count in counter.values():
            if not got_odd and c_count % 2 == 1:
                got_odd = True
                palindrome_len += 1
                c_count -= 1

            pairs = c_count // 2
            if pairs > 0:
                palindrome_len += 2 * pairs

        return palindrome_len


# Runtime: 36 ms, faster than 99.24% of Python3 online submissions for Longest Palindrome.
# Memory Usage: 13.4 MB, less than 6.31% of Python3 online submissions for Longest Palindrome.
