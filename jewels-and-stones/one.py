class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        ret = 0
        for jewel in J:
            ret += S.count(jewel)
            
        return ret
    
# Runtime: 40 ms, faster than 76.78% of Python3 online submissions for Jewels and Stones.
# Memory Usage: 13.3 MB, less than 5.25% of Python3 online submissions for Jewels and Stones.

