class Solution:
    @staticmethod
    def normalize(S: str) -> str:
        even = "".join(sorted(S[::2]))
        odd = "".join(sorted(S[1::2]))
        return even + "|" + odd
    
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        groups = set()
        for word in A:
            groups.add(self.normalize(word))
        
        return len(groups)
        
# Runtime: 44 ms, faster than 80.27% of Python3 online submissions for Groups of Special-Equivalent Strings.
# Memory Usage: 13.4 MB, less than 6.38% of Python3 online submissions for Groups of Special-Equivalent Strings.

