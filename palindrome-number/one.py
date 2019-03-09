class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]
        
# Runtime: 248 ms, faster than 78.29% of Python3 online submissions for Palindrome Number.
# Memory Usage: 13.4 MB, less than 5.03% of Python3 online submissions for Palindrome Number.

