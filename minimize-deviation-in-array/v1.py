from sortedcontainers import SortedList


class Solution:
    @staticmethod
    def is_even(val: int) -> bool:
        return val % 2 == 0

    def minimumDeviation(self, nums: List[int]) -> int:
        num_set = SortedList()
        for num in nums:
            if self.is_even(num):
                num_set.add(num)
            else:
                num_set.add(num * 2)

        min_deviation = num_set[-1] - num_set[0]
        while self.is_even(num_set[-1]):
            num_set.add(round(num_set[-1] / 2))
            num_set.pop()

            new_dev = num_set[-1] - num_set[0]
            min_deviation = min(min_deviation, new_dev)

        return min_deviation


# Runtime: 3374 ms, faster than 5.82% of Python3 online submissions for Minimize Deviation in Array.
# Memory Usage: 27.1 MB, less than 47.57% of Python3 online submissions for Minimize Deviation in Array.
