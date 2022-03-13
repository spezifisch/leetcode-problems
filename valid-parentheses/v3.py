class Solution:
    def isValid(self, s: str) -> bool:
        closers = {
            "(": ")",
            "[": "]",
            "{": "}",
        }
        openers = set(closers.keys())

        opened = ""
        for c in s:
            if c in openers:
                # it's an opener
                opened += c
            else:
                # it's a closer
                if not opened:
                    return False
                if closers[opened[-1]] != c:
                    # wrong closer
                    return False

                opened = opened[:-1]

        if opened:
            return False

        return True


# Runtime: 51 ms, faster than 35.94% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 13.8 MB, less than 82.06% of Python3 online submissions for Valid Parentheses.
