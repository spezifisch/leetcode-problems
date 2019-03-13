class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        A = list(range(len(S) + 1))
        ret = []
        
        for op in S:
            if op == "I":
                ret.append(A.pop(0))
            else:
                ret.append(A.pop())
                
        ret.append(A[0])
        return ret
        
# Runtime: 112 ms, faster than 32.80% of Python3 online submissions for DI String Match.
# Memory Usage: 14.2 MB, less than 5.62% of Python3 online submissions for DI String Match.

