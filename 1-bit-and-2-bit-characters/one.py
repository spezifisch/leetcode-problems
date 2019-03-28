class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        two_bit_started = False
        last_is_one_bit = False
        for bit in bits:
            if not two_bit_started:
                if bit == 1:
                    two_bit_started = True
                    last_is_one_bit = False
                else:
                    last_is_one_bit = True
            else:
                two_bit_started = False
        
        return last_is_one_bit
    
# Runtime: 36 ms, faster than 97.38% of Python3 online submissions for 1-bit and 2-bit Characters.
# Memory Usage: 13.2 MB, less than 11.36% of Python3 online submissions for 1-bit and 2-bit Characters.

