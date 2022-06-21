import sortedcontainers


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        highest_climbs_desc = sortedcontainers.SortedList(key=lambda x: -x)
        highest_climbs_sum = 0
        needed_bricks = 0

        last_height = None
        for i, height in enumerate(heights):
            if i == 0 or height <= last_height:
                # jump down
                last_height = height
                continue

            # climb up
            distance = height - last_height
            highest_climbs_desc.add(distance)
            highest_climbs_sum += distance

            if len(highest_climbs_desc) > ladders:
                smallest = highest_climbs_desc.pop()
                highest_climbs_sum -= smallest
                needed_bricks += smallest

                if needed_bricks > bricks:
                    return i - 1

            last_height = height

        return i


# Runtime: 1572 ms, faster than 6.79% of Python3 online submissions for Furthest Building You Can Reach.
# Memory Usage: 29.3 MB, less than 6.02% of Python3 online submissions for Furthest Building You Can Reach.
