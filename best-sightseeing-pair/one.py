from collections import namedtuple

class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        Poi = namedtuple("Poi", ["score", "index"])
        
        pois = []
        for i, a in enumerate(A):
            pois.append(Poi(score=a, index=i))
            
        pois = sorted(pois, reverse=True, key=lambda p: p.score)
        min_score = pois[-1].score
    
        max_score = 0
        for i, poi_a in enumerate(pois):
            for j, poi_b in enumerate(pois[i+1:]):
                #print(poi_a, poi_b)
                score = poi_a.score + poi_b.score
                if score <= max_score - 1:
                    break
                    
                score -= abs(poi_a.index - poi_b.index)
                
                if score > max_score:
                    max_score = score
                    
                if poi_a.score == poi_b.score and j == 0 and poi_b.score == min_score:
                    return max_score
                    
            if 2*poi_a.score <= max_score:
                break
                    
        return max_score
    
# Runtime: 664 ms, faster than 100.00% of Python3 online submissions for Best Sightseeing Pair.
# Memory Usage: 22 MB, less than 100.00% of Python3 online submissions for Best Sightseeing Pair.

