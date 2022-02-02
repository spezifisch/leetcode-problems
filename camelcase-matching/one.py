class Solution:
    @staticmethod
    def caseSplit(pattern: str) -> List[str]:
        ret = []
        part = ""
        for c in pattern:
            is_upper = c.upper() == c
            if is_upper:
                if part:
                    ret.append(part)
                part = c
            else:
                part += c
        
        if part:
            ret.append(part)
            
        return ret
    
    @staticmethod
    def fuzzyMatch(part: str, pattern: str) -> bool:
        part = list(reversed(part))
        pattern = list(reversed(pattern))
        
        while len(pattern):
            if not len(part):
                return False
            elif part[-1] == pattern[-1]:
                part.pop()
                pattern.pop()
            elif part[-1] == part[-1].lower():
                part.pop()
            else:
                return False
        
        return True
    
    def doesMatch(self, query: str) -> bool:
        pattern_pos = 0
        parts = self.caseSplit(query)
        for part in parts:
            if pattern_pos >= len(self.pattern_parts):
                return False
            
            pattern_part = self.pattern_parts[pattern_pos]
            
            if part.startswith(pattern_part):
                pass
            elif self.fuzzyMatch(part, pattern_part):
                pass
            else:
                return False
            
            pattern_pos += 1
            
        if pattern_pos < len(self.pattern_parts):
            return False

        return True
    
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        self.pattern_parts = self.caseSplit("X" + pattern)
        #print(self.pattern_parts)
        return [self.doesMatch("X" + q) for q in queries]
    
# Runtime: 40 ms, faster than 100.00% of Python3 online submissions for Camelcase Matching.
# Memory Usage: 13.1 MB, less than 100.00% of Python3 online submissions for Camelcase Matching.

