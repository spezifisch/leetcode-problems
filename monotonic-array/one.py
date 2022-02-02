class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        increasing = None
        previous = A[0]
        for elem in A[1:]:
            if elem > previous:
                if increasing == False:
                    return False
                increasing = True
            elif elem < previous:
                if increasing == True:
                    return False
                increasing = False

            previous = elem

        return True


# Runtime: 84 ms, faster than 97.67% of Python3 online submissions for Monotonic Array.
# Memory Usage: 17.3 MB, less than 5.11% of Python3 online submissions for Monotonic Array.
