class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        end = len(s) - 1
        for i in range(len(s) // 2):
            s[i], s[end - i] = s[end - i], s[i]


# Runtime: 209 ms, faster than 82.38% of Python3 online submissions for Reverse String.
# Memory Usage: 18.4 MB, less than 89.54% of Python3 online submissions for Reverse String.
