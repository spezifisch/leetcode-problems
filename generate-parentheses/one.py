class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.results = set()
        self.gen("", o=0, left=n)

        ret = list(self.results)
        # ret.sort()
        return ret

    def gen(self, s, o, left):
        if o > 0:
            s += ")"
            o -= 1

            self.gen(s, o=o, left=left)

        if left == 0:
            s += ")" * o
            o = 0
            self.results.add(s)
            return

        for i in range(1, left + 1):
            part = s + "(" * i
            self.gen(part, o=o + i, left=left - i)


# Runtime: 56 ms, faster than 28.64% of Python3 online submissions for Generate Parentheses.
# Memory Usage: 13.6 MB, less than 5.10% of Python3 online submissions for Generate Parentheses.
