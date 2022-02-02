from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = Counter(s)
        for idx, c in enumerate(s):
            if counts[c] == 1:
                return idx

        return -1


# Runtime: 124 ms, faster than 58.84% of Python3 online submissions for First Unique Character in a String.
# Memory Usage: 13.5 MB, less than 5.04% of Python3 online submissions for First Unique Character in a String.
