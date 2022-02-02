class Solution:
    def isValid(self, s: str) -> bool:
        starts = "({["
        ends = {
            "(": ")",
            "{": "}",
            "[": "]",
        }

        stack = []
        for c in s:
            if not len(stack) or c in starts:
                stack.append(c)
            elif not len(stack):
                return False
            else:
                start = stack.pop()
                if start not in starts:
                    return False
                elif c != ends[start]:
                    return False

        if len(stack):
            return False

        return True


# Runtime: 40 ms, faster than 47.54% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 13 MB, less than 5.22% of Python3 online submissions for Valid Parentheses.
