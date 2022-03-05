from sortedcontainers import SortedSet


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        take_points = {}
        for num in nums:
            take_points[num] = take_points.get(num, 0) + num

        num_set = SortedSet(nums)
        max_prev_points_dist1 = max_prev_points_dist2 = 0
        for i, num in enumerate(num_set):
            if i == 0:
                max_prev_points = 0
            elif num - 1 == num_set[i - 1]:
                # we can't use the number before us
                if i > 1:
                    max_prev_points = max_prev_points_dist2
                else:
                    max_prev_points = 0
            else:
                max_prev_points = max_prev_points_dist1

            num_points = take_points[num] + max_prev_points

            max_prev_points_dist2 = max_prev_points_dist1
            max_prev_points_dist1 = max(max_prev_points_dist1, num_points)

        return max_prev_points_dist1


# Runtime: 60 ms, faster than 84.03% of Python3 online submissions for Delete and Earn.
# Memory Usage: 14.7 MB, less than 26.77% of Python3 online submissions for Delete and Earn.
