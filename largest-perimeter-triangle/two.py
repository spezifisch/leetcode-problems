class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A = sorted(A, reverse=True)
        for i in range(len(A) - 2):
            a, b, c = A[i : i + 3]
            d = b + c
            if a < d:
                return a + d

        return 0


# Runtime: 72 ms, faster than 98.16% of Python3 online submissions for Largest Perimeter Triangle.
# Memory Usage: 13.9 MB, less than 5.10% of Python3 online submissions for Largest Perimeter Triangle.
