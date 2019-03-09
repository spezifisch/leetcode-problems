class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not len(strs) or not len(strs[0]):
            return ""
        if len(strs) == 1:
            return strs[0]
        
        max_i = None
        for i, c in enumerate(strs[0]):
            different = False
            for q in strs[1:]:
                if i >= len(q) or q[i] != c:
                    different = True
                    break
                    
            if different:
                break
                
            max_i = i
        
        if max_i is None:
            return ""
        
        return strs[0][:max_i+1]
    
# Runtime: 40 ms, faster than 69.25% of Python3 online submissions for Longest Common Prefix.
# Memory Usage: 13.3 MB, less than 5.10% of Python3 online submissions for Longest Common Prefix.

