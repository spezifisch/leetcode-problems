class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not len(nums):
            return [[]]

        ret = []
        for i, num in enumerate(nums):
            start = [num]
            remainder = nums[:i] + nums[i + 1 :]
            if len(remainder) >= 2:
                permuts = self.permute(remainder)

                for p in permuts:
                    ret.append(start + p)
            else:
                ret.append(start + remainder)

        return ret


# Runtime: 52 ms, faster than 60.72% of Python3 online submissions for Permutations.
# Memory Usage: 13.3 MB, less than 5.23% of Python3 online submissions for Permutations.
