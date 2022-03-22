class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        # try to get there approximately. fill with "z" and put the rest into "a"
        z_count = int(k / 26)
        xy_val = ""
        a_count = n - z_count

        # get difference to target value of k
        diff = k - (a_count + 26 * z_count)
        # turn "a" to "z" as long as our total is too high by more than 25,
        # turn "z" to "a" in the same way
        while abs(diff) > 25:
            if diff < 0:
                # our total is too high. turn "z" into "a"
                a_count += 1
                z_count -= 1
            else:
                # total too low.
                a_count -= 1
                z_count += 1
            diff = k - (a_count + 26 * z_count)

        # diff is now between -25 and +25. turn an "a" into a letter that absorbs the difference.
        if diff > 0:
            a_count -= 1
            xy_val = chr(ord("a") + diff)
        elif diff < 0:
            z_count -= 1
            xy_val = chr(ord("z") + diff)

        return "a" * a_count + xy_val + "z" * z_count


# Runtime: 67 ms, faster than 85.71% of Python3 online submissions for Smallest String With A Given Numeric Value.
# Memory Usage: 15 MB, less than 87.56% of Python3 online submissions for Smallest String With A Given Numeric Value.
