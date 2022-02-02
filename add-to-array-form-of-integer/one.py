class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        Anum = int("".join(map(str, A)))
        res = K + Anum

        return list(map(int, list(str(res))))


# Runtime: 212 ms, faster than 60.72% of Python3 online submissions for Add to Array-Form of Integer.
# Memory Usage: 14.1 MB, less than 5.12% of Python3 online submissions for Add to Array-Form of Integer.
