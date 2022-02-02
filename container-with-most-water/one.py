class Solution:
    def maxArea(self, height: List[int]) -> int:
        biggest_area = 0

        a = 0
        b = len(height) - 1

        while a <= b:
            left = height[a]
            right = height[b]

            area = (b - a) * min(left, right)
            if area > biggest_area:
                biggest_area = area

            if left > right:
                b -= 1
            else:
                a += 1

        return biggest_area


# Runtime: 60 ms, faster than 87.43% of Python3 online submissions for Container With Most Water.
# Memory Usage: 14.6 MB, less than 5.18% of Python3 online submissions for Container With Most Water.
