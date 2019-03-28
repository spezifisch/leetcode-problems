from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if not ransomNote:
            return True
        if not magazine:
            return False
        
        letters = Counter(magazine)
        for c in ransomNote:
            letters[c] -= 1
            if letters[c] < 0:
                return False
            
        return True
    
# Runtime: 56 ms, faster than 83.46% of Python3 online submissions for Ransom Note.
# Memory Usage: 13.4 MB, less than 6.10% of Python3 online submissions for Ransom Note.

