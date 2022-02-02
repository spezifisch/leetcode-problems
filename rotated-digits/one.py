from decimal import Decimal
from typing import Tuple


class Solution:
    BAD = [3, 4, 7]
    ROTATION = {
        0: 0,
        1: 1,
        2: 5,
        5: 2,
        6: 9,
        8: 8,
        9: 6,
    }

    @staticmethod
    def is_valid(digits: Tuple[int, ...]) -> bool:
        for b in Solution.BAD:
            if b in digits:
                return False

        return True

    @staticmethod
    def rotate_digits(digits: Tuple[int, ...]) -> Tuple[int, ...]:
        return tuple(Solution.ROTATION[digit] for digit in digits)

    @staticmethod
    def is_good(n: int) -> bool:
        digits = Decimal(n).as_tuple().digits
        if not Solution.is_valid(digits):
            return False

        rot = Solution.rotate_digits(digits)
        return digits != rot

    def rotatedDigits(self, N: int) -> int:
        good_count = 0
        for n in range(1, N + 1):
            if self.is_good(n):
                good_count += 1

        return good_count


# Runtime: 224 ms, faster than 8.22% of Python3 online submissions for Rotated Digits.
# Memory Usage: 14.2 MB, less than 6.06% of Python3 online submissions for Rotated Digits.
