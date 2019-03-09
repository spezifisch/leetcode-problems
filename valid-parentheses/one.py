class Solution:
    def isValid(self, s: str) -> bool:
        ends = {
            "(": ")",
            "{": "}",
            "[": "]",
        }
        
        stack = []
        for c in s:
            if not len(stack) or c in ends.keys():
                stack.append(c)
            elif not len(stack):
                return False
            else:
                start = stack.pop()
                if start not in ends.keys():
                    return False
                elif c != ends[start]:
                    return False
        
        if len(stack):
            return False
        
        return True

