class Solution:
    def bitwiseComplement(self, N: int) -> int:
        bits = len(bin(N)) - 2
        mask = int("1" * bits, 2)
        return N ^ mask
   
