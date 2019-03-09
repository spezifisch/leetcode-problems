class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        s = str(x)
        return s == s[::-1]

# Runtime: 272 ms, faster than 60.25% of Python3 online submissions for Palindrome Number.
# Memory Usage: 13.6 MB, less than 5.03% of Python3 online submissions for Palindrome Number.

