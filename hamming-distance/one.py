class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')
    
# Runtime: 44 ms, faster than 32.86% of Python3 online submissions for Hamming Distance.
# Memory Usage: 13.1 MB, less than 5.84% of Python3 online submissions for Hamming Distance.

