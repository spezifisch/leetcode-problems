class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        self.alpha_positions = [i for i, c in enumerate(S) if c.isalpha()]
        letter_count = len(self.alpha_positions)
        if letter_count == 0:
            return [S]
        
        transforms = []
        S = S.lower()
        for i in range(2**letter_count):
            transforms.append(self.transform(S, i))
            
        return transforms
        
    def transform(self, S: str, i: int) -> str:
        one_bit_positions = []
        pos = 0
        while i:
            if (i & 1) == 1:
                one_bit_positions.append(pos)
            
            pos += 1
            i >>= 1
            
        S = list(S)
        for one_bit_pos in one_bit_positions:
            alpha_pos = self.alpha_positions[one_bit_pos]
            S[alpha_pos] = S[alpha_pos].upper()
            
        return "".join(S)
    
# Runtime: 120 ms, faster than 13.80% of Python3 online submissions for Letter Case Permutation.
# Memory Usage: 13.6 MB, less than 26.19% of Python3 online submissions for Letter Case Permutation.

