class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even = []
        odd = []
        for elem in A:
            if elem & 1 == 0:
                even.append(elem)
            else:
                odd.append(elem)
                
        return even + odd
    
# Runtime: 80 ms, faster than 43.41% of Python3 online submissions for Sort Array By Parity.
# Memory Usage: 14 MB, less than 5.69% of Python3 online submissions for Sort Array By Parity.

