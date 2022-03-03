class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        ans = 0
        diff_streak = 0
        prev_diff = None
        prev_num = None
        for num in nums:
            if prev_num is None:
                # 1st round
                pass
            elif prev_diff is None:
                # 2nd round
                prev_diff = num - prev_num
            else:
                # 3+
                diff = num - prev_num

                if diff == prev_diff:
                    diff_streak += 1

                    ans += diff_streak
                    # print(f"diff={diff} streak={diff_streak} ans={ans}")
                else:
                    diff_streak = 0
                    # print(f"diff={diff} streak reset")

                prev_diff = diff

            prev_num = num

        return ans


# Runtime: 51 ms, faster than 58.95% of Python3 online submissions for Arithmetic Slices.
# Memory Usage: 14.1 MB, less than 97.59% of Python3 online submissions for Arithmetic Slices.
