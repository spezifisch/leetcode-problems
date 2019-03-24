class Solution:    
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        N = len(points)
        
        max_area = 0
        for i in range(N):
            A = points[i]
            
            for j in range(N):
                if i == j:
                    continue
                
                B = points[j]
                    
                for k in range(N):
                    if i == k or j == k:
                        continue
                        
                    C = points[k]
                    area = 0.5 * abs(A[0]*B[1] + B[0]*C[1] + C[0]*A[1] - B[0]*A[1] - C[0]*B[1] - A[0]*C[1])

                    if area > max_area:
                        max_area = area
                    
        return max_area

# Runtime: 700 ms, faster than 8.46% of Python3 online submissions for Largest Triangle Area.
# Memory Usage: 13.3 MB, less than 6.67% of Python3 online submissions for Largest Triangle Area.

