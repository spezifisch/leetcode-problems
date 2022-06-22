class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]


# Runtime: 101 ms, faster than 51.47% of Python3 online submissions for Kth Largest Element in an Array.
# Memory Usage: 14.9 MB, less than 40.87% of Python3 online submissions for Kth Largest Element in an Array.
