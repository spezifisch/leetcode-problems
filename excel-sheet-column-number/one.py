class Solution:
    def titleToNumber(self, s: str) -> int:
        val = 0
        for exp, c in enumerate(s[::-1]):
            val += (1 + ord(c) - ord("A")) * 26**exp

        return val


# Runtime: 56 ms, faster than 73.69% of Python3 online submissions for Excel Sheet Column Number.
# Memory Usage: 13.5 MB, less than 5.44% of Python3 online submissions for Excel Sheet Column Number.
