class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split(".")))
        v2 = list(map(int, version2.split(".")))

        ldiff = len(v1) - len(v2)
        if ldiff > 0:  # v1 is longer
            v2 += [0] * ldiff
        elif ldiff < 0:  # v2 is longer
            v1 += [0] * -ldiff

        for i in range(len(v1)):
            place_diff = v1[i] - v2[i]
            if place_diff > 0:
                return 1
            elif place_diff < 0:
                return -1

        return 0


# Runtime: 42 ms, faster than 52.71% of Python3 online submissions for Compare Version Numbers.
# Memory Usage: 13.9 MB, less than 68.52% of Python3 online submissions for Compare Version Numbers.
