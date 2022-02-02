class Solution:
    @staticmethod
    def swappable(A, B, swap_first=False):
        wanted = A[0]
        swap = 0

        if swap_first:
            swap = 1
            wanted = B[0]

        for i in range(1, len(A)):
            if A[i] == wanted:
                pass
            elif B[i] == wanted:
                swap += 1
            else:
                return -1

        return swap

    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        one = Solution.swappable(A, B)
        one_b = Solution.swappable(A, B, True)
        two = Solution.swappable(B, A)
        two_b = Solution.swappable(B, A, True)

        solutions = [one, one_b, two, two_b]
        solutions = list(filter(lambda x: x >= 0, solutions))

        if not len(solutions):
            return -1
        return min(solutions)
