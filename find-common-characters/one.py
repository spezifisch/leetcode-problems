from collections import defaultdict

class Solution:
    @staticmethod
    def getWordHistogram(word: str) -> defaultdict:
        hist = defaultdict(lambda: 0)
        for c in word:
            hist[c] += 1
            
        return hist
    
    @staticmethod
    def getMinimumHistogram(hists: List[defaultdict]) -> dict:
        if not len(hists):
            return {}
        
        merge = dict(hists[0])
        for hist in hists[1:]:
            merge_deletions = []
            for key in merge.keys():
                if key in hist:
                    merge[key] = min(merge[key], hist[key])
                else:
                    merge_deletions.append(key)
                    
            for merge_key in merge_deletions:
                del merge[merge_key]
                    
        return merge
    
    def commonChars(self, A: List[str]) -> List[str]:
        hists = []
        for word in A:
            hist = Solution.getWordHistogram(word)
            hists.append(hist)
            
        min_hist = Solution.getMinimumHistogram(hists)
        
        ret = []
        for letter, count in min_hist.items():
            ret += [letter] * count
        
        return ret
        
# Runtime: 60 ms, faster than 80.03% of Python3 online submissions for Find Common Characters.
# Memory Usage: 13.4 MB, less than 100.00% of Python3 online submissions for Find Common Characters.

