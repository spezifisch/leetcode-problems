class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        nums_idx_to_rank = dict()
        best = sorted(enumerate(nums), key=lambda x: x[1], reverse=True)
        for place, num in enumerate(best, start=1):
            nums_idx = num[0]
            if place == 1:
                rank = "Gold Medal"
            elif place == 2:
                rank = "Silver Medal"
            elif place == 3:
                rank = "Bronze Medal"
            else:
                rank = str(place)
                
            nums_idx_to_rank[nums_idx] = rank
            
        return [nums_idx_to_rank[idx] for idx in range(len(nums))]
    
# Runtime: 76 ms, faster than 53.10% of Python3 online submissions for Relative Ranks.
# Memory Usage: 14.5 MB, less than 9.52% of Python3 online submissions for Relative Ranks.

