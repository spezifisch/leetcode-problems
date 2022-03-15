class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        out = ""
        opened = 0

        for c in s:
            if c == ")":
                if opened > 0:
                    opened -= 1
                    out += c
                else:
                    pass
            elif c == "(":
                opened += 1
                out += c
            else:
                out += c

        if opened > 0:
            parts = out.rsplit("(", opened)
            out = "".join(parts)

        return out


# Runtime: 115 ms, faster than 81.72% of Python3 online submissions for Minimum Remove to Make Valid Parentheses.
# Memory Usage: 15.2 MB, less than 96.63% of Python3 online submissions for Minimum Remove to Make Valid Parentheses.
