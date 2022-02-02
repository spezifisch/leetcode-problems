class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        return list(zip(*A))


# Runtime: 76 ms, faster than 26.57% of Python3 online submissions for Transpose Matrix.
# Memory Usage: 13.5 MB, less than 5.45% of Python3 online submissions for Transpose Matrix.
