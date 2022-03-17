class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        if len(s) == 2:
            return 1

        ret = 0
        open_count = 0
        part = ""
        for c in s:
            if c == "(":
                open_count += 1
            elif c == ")":
                open_count -= 1

            part += c
            if open_count == 0:
                if len(part) == 2:
                    ret += 1
                else:
                    part = part[1:-1]
                    ret += 2 * self.scoreOfParentheses(part)

                part = ""

        return ret


# Runtime: 41 ms, faster than 59.02% of Python3 online submissions for Score of Parentheses.
# Memory Usage: 13.8 MB, less than 98.59% of Python3 online submissions for Score of Parentheses.
