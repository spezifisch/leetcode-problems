from bisect import bisect_left


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return []

        len_numbers = len(numbers)
        for i, num in enumerate(numbers):
            wanted = target - num
            if wanted > i:
                idx = bisect_left(numbers, wanted, i + 1, len_numbers)
                if idx != len_numbers and numbers[idx] == wanted:
                    return [1 + i, 1 + idx]
            elif wanted < i:
                idx = bisect_left(numbers, wanted, 0, i)
                if idx != len_numbers and numbers[idx] == wanted:
                    return [1 + idx, 1 + i]

        return []


# Runtime: 44 ms, faster than 50.43% of Python3 online submissions for Two Sum II - Input array is sorted.
# Memory Usage: 13.4 MB, less than 5.14% of Python3 online submissions for Two Sum II - Input array is sorted.
