class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        last_num = None
        cur_start = None
        ranges = []

        for num in nums + [None]:
            if num is None:
                if last_num is None:
                    cur_start = num
                    last_num = num

            if last_num is None:
                cur_start = num
            elif last_num + 1 == num:
                pass
            else:
                try:
                    diff = num - cur_start
                except TypeError:
                    diff = 23

                if diff > 1 and cur_start != last_num:
                    ranges.append(f"{cur_start}->{last_num}")
                else:
                    ranges.append(str(last_num))

                cur_start = num

            last_num = num

        return ranges


# Runtime: 32 ms, faster than 84.38% of Python3 online submissions for Summary Ranges.
# Memory Usage: 13.9 MB, less than 88.25% of Python3 online submissions for Summary Ranges.
