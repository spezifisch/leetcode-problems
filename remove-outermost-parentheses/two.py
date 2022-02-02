class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        ret = ""

        part = ""
        p_open = 0
        for c in S:
            part += c

            if c == "(":
                p_open += 1
            else:
                p_open -= 1

                if p_open == 0:
                    ret += part[1:-1]
                    part = ""

        return ret


# Runtime: 44 ms, faster than 100.00% of Python3 online submissions for Remove Outermost Parentheses.
# Memory Usage: 13.1 MB, less than 100.00% of Python3 online submissions for Remove Outermost Parentheses.
