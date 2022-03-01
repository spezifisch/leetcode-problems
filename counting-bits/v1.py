class Solution:
    def countBits(self, n: int) -> List[int]:
        return [bin(x).count("1") for x in range(n + 1)]


# Runtime: 140 ms, faster than 45.48% of Python3 online submissions for Counting Bits.
# Memory Usage: 20.8 MB, less than 87.66% of Python3 online submissions for Counting Bits.
