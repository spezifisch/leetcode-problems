class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        specials = dict()
        string = []
        for i, c in enumerate(S):
            if "a" <= c <= "z" or "A" <= c <= "Z":
                string.append(c)
            else:
                specials[i] = c

        string.reverse()
        for pos in sorted(specials.keys()):
            string.insert(pos, specials[pos])

        return "".join(string)


# Runtime: 40 ms, faster than 59.07% of Python3 online submissions for Reverse Only Letters.
# Memory Usage: 13.3 MB, less than 5.56% of Python3 online submissions for Reverse Only Letters.
