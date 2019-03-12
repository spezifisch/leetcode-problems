class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        origK = K
        current_len = longest = 0
        i = 0
        for j in range(len(A)):
            current_len += 1
            
            if A[j] == 1:
                pass
            elif A[j] == 0:
                if K > 0:
                    K -= 1
                else:
                    for x in range(i, j + 1):
                        current_len -= 1
                        if A[x] == 0:
                            i = x + 1
                            break
                    
            if current_len > longest:
                longest = current_len
                
        return longest

# Runtime: 164 ms, faster than 78.43% of Python3 online submissions for Max Consecutive Ones III.
# Memory Usage: 13.6 MB, less than 100.00% of Python3 online submissions for Max Consecutive Ones III.

