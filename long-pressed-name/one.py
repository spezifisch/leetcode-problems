class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if not name:
            return True
        if not typed:
            return False
        
        name = list(reversed(name))
        typed = list(reversed(typed))
        last_name_char = None
        while len(name):
            if not len(typed):
                return False
            elif name[-1] == typed[-1]:
                last_name_char = name.pop()
                typed.pop()
            elif last_name_char == typed[-1]:
                typed.pop()
            else:
                return False
            
        return True
    
# Runtime: 40 ms, faster than 55.36% of Python3 online submissions for Long Pressed Name.
# Memory Usage: 13 MB, less than 7.84% of Python3 online submissions for Long Pressed Name.

