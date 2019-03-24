class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        Asum = sum(A)
        Asum3 = Asum // 3
        if (Asum % 3) != 0:
            return False
        
        part_sum = 0
        parts = 0
        for num in A:
            #print(part_sum, "+=", num)
            part_sum += num
            
            if part_sum == Asum3:
                part_sum = 0
                parts += 1
            
        return parts == 3
        
# Runtime: 72 ms, faster than 100.00% of Python3 online submissions for Partition Array Into Three Parts With Equal Sum.
# Memory Usage: 17.9 MB, less than 100.00% of Python3 online submissions for Partition Array Into Three Parts With Equal Sum.

