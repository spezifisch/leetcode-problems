class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split(".")))
        v2 = list(map(int, version2.split(".")))

        for i in range(max(len(v1), len(v2))):
            a = v1[i : i + 1] or [0]
            b = v2[i : i + 1] or [0]
            place_diff = a[0] - b[0]
            if place_diff > 0:
                return 1
            elif place_diff < 0:
                return -1

        return 0


# Runtime: 51 ms, faster than 28.81% of Python3 online submissions for Compare Version Numbers.
# Memory Usage: 13.9 MB, less than 68.52% of Python3 online submissions for Compare Version Numbers.
