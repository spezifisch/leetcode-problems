class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        ret = [None] * len(S)

        idx = 0
        distance = None
        for char in S:
            if char == C:
                distance = 0
            elif distance is not None:
                distance += 1

            if distance is not None:
                ret[idx] = distance

            idx += 1

        distance = None
        for idx in range(len(S) - 1, -1, -1):
            char = S[idx]
            if char == C:
                distance = 0
            elif distance is not None:
                distance += 1

            if distance is not None:
                if ret[idx] is None or distance < ret[idx]:
                    ret[idx] = distance

        return ret


# Runtime: 52 ms, faster than 72.69% of Python3 online submissions for Shortest Distance to a Character.
# Memory Usage: 13.1 MB, less than 5.56% of Python3 online submissions for Shortest Distance to a Character.
