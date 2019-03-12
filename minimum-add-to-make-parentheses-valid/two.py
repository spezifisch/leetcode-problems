class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        inserted = 0
        o = 0
        for s in S:
            if s == "(":
                o += 1
            elif s == ")":
                o -= 1
                
                if o < 0:
                    inserted += 1
                    o = 0
                    
        if o > 0:
            inserted += o
                
        return inserted
        
# Runtime: 40 ms, faster than 57.08% of Python3 online submissions for Minimum Add to Make Parentheses Valid.
# Memory Usage: 13.1 MB, less than 5.17% of Python3 online submissions for Minimum Add to Make Parentheses Valid.

