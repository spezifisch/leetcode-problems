class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")

        for i in range(max(len(v1), len(v2))):
            try:
                a = int(v1[i])
            except IndexError:
                a = 0
            try:
                b = int(v2[i])
            except IndexError:
                b = 0
            place_diff = a - b
            if place_diff > 0:
                return 1
            elif place_diff < 0:
                return -1

        return 0


# Runtime: 66 ms, faster than 5.52% of Python3 online submissions for Compare Version Numbers.
# Memory Usage: 13.9 MB, less than 92.33% of Python3 online submissions for Compare Version Numbers.
