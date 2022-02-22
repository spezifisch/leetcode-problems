class Solution:
    def titleToNumber(self, columnTitle: str | list[str]) -> int:
        num = 0
        for i, c in enumerate(columnTitle[::-1]):
            val = ord(c) - ord("A") + 1
            num += val * 26**i

        return num


# Runtime: 55 ms, faster than 29.73% of Python3 online submissions for Excel Sheet Column Number.
# Memory Usage: 13.8 MB, less than 98.67% of Python3 online submissions for Excel Sheet Column Number.
