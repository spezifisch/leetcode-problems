class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        primes = [2, 3, 5, 7, 11, 13, 17, 19]  # ,23,29,31]

        count = 0
        for i in range(L, R + 1):
            bits = self.bitsSet(i)
            if bits in primes:
                count += 1

        return count

    @staticmethod
    def bitsSet(val: int, maxBits: int = 20) -> int:
        bits = 0
        for i in range(maxBits):
            if val & (1 << i):
                bits += 1

        return bits


# Runtime: 1168 ms, faster than 17.37% of Python3 online submissions for Prime Number of Set Bits in Binary Representation.
# Memory Usage: 12.8 MB, less than 5.55% of Python3 online submissions for Prime Number of Set Bits in Binary Representation.
