class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if not N:
            return -1
        if N == 1 and trust:
            return -1
        
        edge_to = [set() for _ in range(N)]
        trusted_count = [0] * N
        
        for a, b in trust:
            a -= 1
            b -= 1
            
            if b not in edge_to[a]:
                edge_to[a].add(b)
                trusted_count[b] += 1
                
        judges = []
        for i, trusted in enumerate(edge_to):
            if not len(trusted):
                if trusted_count[i] == N - 1:
                    judges.append(i)
                
        if len(judges) != 1:
            return -1
        
        return 1 + judges[0]
            
# Runtime: 124 ms, faster than 51.17% of Python3 online submissions for Find the Town Judge.
# Memory Usage: 16.2 MB, less than 100.00% of Python3 online submissions for Find the Town Judge.

