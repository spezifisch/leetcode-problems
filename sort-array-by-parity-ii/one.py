class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        even = []
        odd = []
        for i in range(len(A)):
            if A[i] % 2 == 0:
                even.append(A[i])
            else:
                odd.append(A[i])
        
        ret = []
        for i in range(len(A) // 2):
            ret.append(even[i])
            ret.append(odd[i])
            
        return ret
        
# Runtime: 172 ms, faster than 35.82% of Python3 online submissions for Sort Array By Parity II.
# Memory Usage: 15.7 MB, less than 5.49% of Python3 online submissions for Sort Array By Parity II.

