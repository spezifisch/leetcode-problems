class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        A = list(range(len(S) + 1))
        pos_left = 0
        pos_right = len(A) - 1
        ret = []

        for op in S:
            if op == "I":
                ret.append(A[pos_left])
                pos_left += 1
            else:
                ret.append(A[pos_right])
                pos_right -= 1

        ret.append(A[pos_left])
        return ret


# Runtime: 92 ms, faster than 62.78% of Python3 online submissions for DI String Match.
# Memory Usage: 14.2 MB, less than 5.62% of Python3 online submissions for DI String Match.
