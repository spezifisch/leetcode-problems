from bisect import bisect_left


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        idx = bisect_left(nums, target)
        if idx < len(nums) and target == nums[idx]:
            return idx

        return -1


# Runtime: 48 ms, faster than 91.68% of Python3 online submissions for Binary Search.
# Memory Usage: 14 MB, less than 5.19% of Python3 online submissions for Binary Search.
