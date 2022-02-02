from itertools import count


class Solution:
    def findNext(self, seed: str) -> int:
        pos = None
        while True:
            pos = self.s.find(seed, pos)
            if pos < 0:
                return

            yield pos
            pos += 1

    def getChainCount(self, seed: str) -> int:
        a, b = seed[0], seed[-1]
        seed_end_offset = len(seed) - 1
        num = 0

        for pos in self.findNext(seed):
            num += 1

            for expand in count(1):
                start = pos - expand
                end = pos + seed_end_offset + expand

                if start < 0 or end >= self.s_len:
                    break

                if self.s[start] != a or self.s[end] != b:
                    break

                num += 1

        return num

    def countBinarySubstrings(self, s: str) -> int:
        self.s = s
        self.s_len = len(s)
        return self.getChainCount("01") + self.getChainCount("10")


# Runtime: 292 ms, faster than 16.54% of Python3 online submissions for Count Binary Substrings.
# Memory Usage: 13.4 MB, less than 14.93% of Python3 online submissions for Count Binary Substrings.
