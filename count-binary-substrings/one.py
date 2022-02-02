class Solution:
    def getChainCount(self, chain: str) -> int:
        count = 0
        lcnt = None
        while lcnt is None or lcnt > 0:
            lcnt = self.s.count(chain)
            count += lcnt
            chain = chain[0] + chain + chain[-1]

        return count

    def countBinarySubstrings(self, s: str) -> int:
        self.s = s
        return self.getChainCount("01") + self.getChainCount("10")


# Time Limit Exceeded
