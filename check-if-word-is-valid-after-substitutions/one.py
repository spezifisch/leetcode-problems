class Solution:
    def isValid(self, S: str) -> bool:
        while len(S) > 0:
            place = S.find("abc")
            if place < 0:
                break
                
            S = S[:place] + S[place + 3:]
            
        if len(S) > 0:
            return False
        
        return True
    
