from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(lambda: [])
        
        for word in strs:
            alphabetical = "".join(sorted(word))
            d[alphabetical].append(word)
            
        return list(d.values())
            
# Runtime: 116 ms, faster than 80.60% of Python3 online submissions for Group Anagrams.
# Memory Usage: 16.1 MB, less than 32.91% of Python3 online submissions for Group Anagrams.

