class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        biggest_pos = []
        smallest_neg = []
        for a in A:
            if a >= 0:
                biggest_pos.append(a)
            else:
                smallest_neg.append(a)
                
        smallest_neg.sort()
        
        k_left = K
        for i in range(len(smallest_neg)):
            if k_left > 0:
                smallest_neg[i] = -smallest_neg[i]
                k_left -= 1
            else:
                break
                
        if k_left > 0:
            new_a = biggest_pos + smallest_neg
            new_a.sort()
            if k_left % 2 == 1:
                new_a[0] = -new_a[0]
            
            return sum(new_a)
        
        return sum(biggest_pos + smallest_neg)
        
