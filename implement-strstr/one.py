class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_hay = len(haystack)
        len_needle = len(needle)

        for offset in range(len_hay - len_needle + 1):
            if needle == haystack[offset : offset + len_needle]:
                return offset

        return -1


# Runtime: 52 ms, faster than 39.74% of Python3 online submissions for Implement strStr().
# Memory Usage: 13.3 MB, less than 5.13% of Python3 online submissions for Implement strStr().
