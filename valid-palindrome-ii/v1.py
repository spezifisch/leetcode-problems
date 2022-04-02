class Solution:
    def validPalindrome(self, s: str, deletable: bool = True) -> bool:
        for i in range(len(s) // 2):
            j = len(s) - 1 - i
            if s[i] != s[j]:
                if deletable:
                    a = s[i + 1 : j + 1]
                    b = s[i:j]
                    return self.validPalindrome(a, False) or self.validPalindrome(
                        b, False
                    )
                else:
                    return False

        return True


# Runtime: 270 ms, faster than 23.38% of Python3 online submissions for Valid Palindrome II.
# Memory Usage: 14.5 MB, less than 52.23% of Python3 online submissions for Valid Palindrome II.
