class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        o = n << 1
        if n & 1 == 0:
            o |= 1

        mask = o
        resto = o
        while resto:
            resto >>= 1
            mask |= resto

        return (n ^ o) == mask


# Runtime: 40 ms, faster than 64.05% of Python3 online submissions for Binary Number with Alternating Bits.
# Memory Usage: 13.1 MB, less than 6.67% of Python3 online submissions for Binary Number with Alternating Bits.
