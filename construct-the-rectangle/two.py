from math import sqrt, floor

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        for w in range(int(floor(sqrt(area))), 0, -1):
            if (area % w) == 0:
                l = area // w
                return [l, w]
        
# Runtime: 36 ms, faster than 93.05% of Python3 online submissions for Construct the Rectangle.
# Memory Usage: 13.1 MB, less than 11.11% of Python3 online submissions for Construct the Rectangle.

