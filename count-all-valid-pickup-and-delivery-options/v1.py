class Solution:
    @staticmethod
    def arithmetic_sum(end: int, start: int = 1) -> int:
        return int(end / 2 * (start + end))

    @staticmethod
    def limit(val: int | float) -> int:
        return int(val % (1e9 + 7))

    def countOrders(self, n: int) -> int:
        slots = 1
        possibilities = 1
        for i in range(2, n + 1):
            slots += 2
            possibilities = self.limit(possibilities * self.arithmetic_sum(slots))

        return possibilities


# Runtime: 52 ms, faster than 49.43% of Python3 online submissions for Count All Valid Pickup and Delivery Options.
# Memory Usage: 14 MB, less than 71.02% of Python3 online submissions for Count All Valid Pickup and Delivery Options.
