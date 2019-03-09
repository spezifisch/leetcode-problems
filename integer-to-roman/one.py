class Solution:
    def intToRoman(self, num: int) -> str:
        decimals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        
        ret = ""
        for (decimal, letter) in zip(decimals, romans):
            letter_count = num // decimal
            ret += letter_count * letter
            
            num -= letter_count * decimal
        
        return ret
    
# Runtime: 144 ms, faster than 46.59% of Python3 online submissions for Integer to Roman.
# Memory Usage: 13.5 MB, less than 5.14% of Python3 online submissions for Integer to Roman.

