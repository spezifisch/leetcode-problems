class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for row in range(len(A)):
            A[row] = [1 if x == 0 else 0 for x in A[row][::-1]]

        return A


# Runtime: 48 ms, faster than 67.42% of Python3 online submissions for Flipping an Image.
# Memory Usage: 13.3 MB, less than 5.63% of Python3 online submissions for Flipping an Image.
