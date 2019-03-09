import decimal

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        d = decimal.Decimal(x).as_tuple().digits
        return d == d[::-1]

# Runtime: 248 ms, faster than 78.29% of Python3 online submissions for Palindrome Number.
# Memory Usage: 13.3 MB, less than 5.03% of Python3 online submissions for Palindrome Number.

