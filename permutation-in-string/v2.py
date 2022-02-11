class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)

        for i in range(len(s2) - len(s1) + 1):
            if s1 == sorted(s2[i : i + len(s1)]):
                return True

        return False


# Runtime: 6048 ms, faster than 8.68% of Python3 online submissions for Permutation in String.
# Memory Usage: 14.1 MB, less than 83.82% of Python3 online submissions for Permutation in String.
