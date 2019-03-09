class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        used = set()
        for elem in A:
            if elem in used:
                return elem
            used.add(elem)
            
# Runtime: 48 ms, faster than 84.85% of Python3 online submissions for N-Repeated Element in Size 2N Array.
# Memory Usage: 14.1 MB, less than 5.12% of Python3 online submissions for N-Repeated Element in Size 2N Array.

