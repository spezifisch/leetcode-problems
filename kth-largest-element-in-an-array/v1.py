import sortedcontainers


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        sl = sortedcontainers.SortedList()

        for num in nums:
            sl.add(num)

        return sl[-k]


# Runtime: 169 ms, faster than 18.21% of Python3 online submissions for Kth Largest Element in an Array.
# Memory Usage: 15.2 MB, less than 18.06% of Python3 online submissions for Kth Largest Element in an Array.
