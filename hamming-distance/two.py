class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y
        dist = 0
        for i in range(32):
            if z & (1<<i):
                dist += 1
                
        return dist
    
# Runtime: 40 ms, faster than 50.05% of Python3 online submissions for Hamming Distance.
# Memory Usage: 13 MB, less than 5.84% of Python3 online submissions for Hamming Distance.

