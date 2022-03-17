class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        if s == "()":
            return 1

        ret = 0
        open_count = 0
        part = ""
        for c in s:
            if c == "(":
                open_count += 1
            elif c == ")":
                open_count -= 1
            else:
                assert False

            assert open_count >= 0

            part += c
            if open_count == 0:
                if len(part) == 2:
                    ret += 1
                else:
                    part = part[1:-1]
                    ret += 2 * self.scoreOfParentheses(part)

                part = ""

        assert open_count == 0
        return ret


# Runtime: 58 ms, faster than 13.53% of Python3 online submissions for Score of Parentheses.
# Memory Usage: 14 MB, less than 30.17% of Python3 online submissions for Score of Parentheses.
