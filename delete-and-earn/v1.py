from sortedcontainers import SortedSet


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        take_points = {}
        for num in nums:
            take_points[num] = take_points.get(num, 0) + num

        num_set = SortedSet(nums)
        points = []
        for i, num in enumerate(num_set):
            if i == 0:
                max_prev_points = 0
            elif num - 1 == num_set[i - 1]:
                # we can't use the number before us
                if i > 1:
                    max_prev_points = max(points[:-1])
                else:
                    max_prev_points = 0
            else:
                max_prev_points = max(points)

            num_points = take_points[num] + max_prev_points
            points.append(num_points)

        return max(points)


# Runtime: 135 ms, faster than 15.55% of Python3 online submissions for Delete and Earn.
# Memory Usage: 14.8 MB, less than 14.49% of Python3 online submissions for Delete and Earn.
