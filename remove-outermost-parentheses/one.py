class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        decomp_parts = []
        p_open = 0
        part = ""
        for c in S:
            part += c
            if c == "(":
                p_open += 1
            else:
                p_open -= 1

                if p_open == 0:
                    decomp_parts.append(part)
                    part = ""

        ret = ""
        for part in decomp_parts:
            ret += part[1:-1]

        return ret


# Runtime: 44 ms, faster than 100.00% of Python3 online submissions for Remove Outermost Parentheses.
# Memory Usage: 13.3 MB, less than 100.00% of Python3 online submissions for Remove Outermost Parentheses.
