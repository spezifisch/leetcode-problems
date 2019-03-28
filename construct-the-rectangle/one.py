from math import sqrt, ceil
from itertools import count

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        for l in count(int(ceil(sqrt(area)))):
            if (area % l) == 0:
                w = area // l
                return [l, w]
        
# Runtime: 1204 ms, faster than 19.90% of Python3 online submissions for Construct the Rectangle.
# Memory Usage: 13.2 MB, less than 11.11% of Python3 online submissions for Construct the Rectangle.

