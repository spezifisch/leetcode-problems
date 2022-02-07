class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        assert len(t) == len(s) + 1
        s = sorted(s)
        t = sorted(t)
        for i, s_val in enumerate(s):
            if s_val != t[i]:
                return t[i]

        return t[-1]


# Runtime: 63 ms, faster than 19.07% of Python3 online submissions for Find the Difference.
# Memory Usage: 14 MB, less than 88.02% of Python3 online submissions for Find the Difference.
