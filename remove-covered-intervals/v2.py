from sortedcontainers import SortedDict, SortedSet


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        remaining = len(intervals)

        ints = SortedDict()
        for interval in intervals:
            start, end = interval

            ends = ints.get(start)
            if ends is None:
                ends = SortedSet()
            elif end in ends:
                # duplicated range removed
                remaining -= 1

            ends.add(end)
            ints[start] = ends

        for start_idx, start in enumerate(ints.keys()):
            ends = ints[start]
            other_starts = ints.keys()[: start_idx + 1]
            for end in ends:
                removed_it = False

                # get intervals with same or lower start number
                for other_start in other_starts:
                    other_ends = ints[other_start]

                    is_same_start = start == other_start
                    for other_end in other_ends.irange(
                        minimum=end, inclusive=(not is_same_start, True)
                    ):
                        remaining -= 1
                        removed_it = True
                        break

                    if removed_it:
                        break

        return remaining


# Runtime: 670 ms, faster than 5.20% of Python3 online submissions for Remove Covered Intervals.
# Memory Usage: 16.2 MB, less than 7.79% of Python3 online submissions for Remove Covered Intervals.
