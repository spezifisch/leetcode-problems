class Solution:
    def toLowerCase(self, s: str) -> str:
        rets = list(s)
        for i in range(len(s)):
            os = s[i]
            if "A" <= os <= "Z":
                rets[i] = chr(ord(os) + 32)

        return "".join(rets)


# Runtime: 36 ms, faster than 54.93% of Python3 online submissions for To Lower Case.
# Memory Usage: 13.3 MB, less than 5.45% of Python3 online submissions for To Lower Case.
