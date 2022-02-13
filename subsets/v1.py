class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        paths = [[]]
        while len(nums):
            num = nums.pop()

            new_paths = []
            for path in paths:
                new_paths.append(path + [num])

            paths += new_paths

        return paths


# Runtime: 47 ms, faster than 48.32% of Python3 online submissions for Subsets.
# Memory Usage: 14.2 MB, less than 82.34% of Python3 online submissions for Subsets.
