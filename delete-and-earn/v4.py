from collections import Counter
from sortedcontainers import SortedSet


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # count how often each number occurs (for calculating points)
        counts = Counter(nums)
        # remove duplicate numbers and sort
        num_set = SortedSet(nums)
        # saves the maximum points up when taking the previous number and the number before it
        max_points_dist1 = max_points_dist2 = 0

        for i, num in enumerate(num_set):
            # calculate maximum points we can get when taking `num`

            if i == 0:
                # there are no previous numbers yet
                max_prev_points = 0
            elif num - 1 == num_set[i - 1]:
                # note: num_set is an ordered list.
                # we can't use the number before us because its value is (num - 1).
                if i > 1:
                    max_prev_points = max_points_dist2
                else:
                    # special case at start of array
                    max_prev_points = 0
            else:
                max_prev_points = max_points_dist1

            # points for num + maximum points for the previous number we're allowed to take
            num_points = num * counts[num] + max_prev_points

            max_points_dist2 = max_points_dist1
            max_points_dist1 = max(max_points_dist1, num_points)

        return max_points_dist1


# Runtime: 79 ms, faster than 60.27% of Python3 online submissions for Delete and Earn.
# Memory Usage: 14.8 MB, less than 14.49% of Python3 online submissions for Delete and Earn.
