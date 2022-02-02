from collections import deque


class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        A = deque(range(len(S) + 1))
        ret = []

        for op in S:
            if op == "I":
                ret.append(A.popleft())
            else:
                ret.append(A.pop())

        ret.append(A[0])
        return ret


# Runtime: 92 ms, faster than 62.78% of Python3 online submissions for DI String Match.
# Memory Usage: 14.4 MB, less than 5.62% of Python3 online submissions for DI String Match.
