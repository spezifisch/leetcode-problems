from math import sqrt

class Solution:
    @staticmethod
    def distance(A: List[int], B: List[int]) -> float:
        return sqrt((A[0] - B[0])**2 + (A[1] - B[1])**2)
    
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        N = len(points)
        
        max_area_sqr = 0
        for i in range(N):
            A = points[i]
            
            for j in range(N):
                if i == j:
                    continue
                
                B = points[j]
                l1 = self.distance(A, B)
                    
                for k in range(N):
                    if i == k or j == k:
                        continue
                        
                    C = points[k]
                    l2 = self.distance(A, C)
                    l3 = self.distance(B, C)
                    l = (l1 + l2 + l3) / 2
                    area_sqr = l * (l - l1) * (l - l2) * (l - l3)

                    if area_sqr > max_area_sqr:
                        max_area_sqr = area_sqr
                    
        return sqrt(max_area_sqr)

# Runtime: 1660 ms, faster than 5.14% of Python3 online submissions for Largest Triangle Area.
# Memory Usage: 12.9 MB, less than 20.00% of Python3 online submissions for Largest Triangle Area.

