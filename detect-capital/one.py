class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        first_big = word[0].upper() == word[0]
        rest_small = rest_big = True

        for c in word[1:]:
            if c.upper() != c:
                rest_big = False
            if c.lower() != c:
                rest_small = False

            if not rest_small and not rest_big:
                break

        if first_big:
            if rest_big or rest_small:
                return True
            return False
        else:
            # first is small
            if rest_small:
                return True

        return False


# Runtime: 52 ms, faster than 36.39% of Python3 online submissions for Detect Capital.
# Memory Usage: 13.3 MB, less than 6.19% of Python3 online submissions for Detect Capital.
