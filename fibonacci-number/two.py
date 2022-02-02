class Solution:
    def __init__(self):
        self.cache = {
            0: 0,
            1: 1,
            2: 1,
            3: 2,
            4: 3,
            5: 5,
            6: 8,
            7: 13,
            8: 21,
            9: 34,
            10: 55,
            11: 89,
            12: 144,
            13: 233,
            14: 377,
            15: 610,
            16: 987,
            17: 1597,
            18: 2584,
            19: 4181,
            20: 6765,
            21: 10946,
            22: 17711,
            23: 28657,
            24: 46368,
            25: 75025,
            26: 121393,
            27: 196418,
            28: 317811,
            29: 514229,
            30: 832040,
        }

    def fib(self, N: int) -> int:
        if N in self.cache:
            return self.cache[N]

        a = self.cache.get(N - 1, self.fib(N - 1))
        b = self.cache.get(N - 2, self.fib(N - 2))
        self.cache[N] = a + b
        return self.cache[N]


# Runtime: 36 ms, faster than 65.38% of Python3 online submissions for Fibonacci Number.
# Memory Usage: 13.1 MB, less than 5.02% of Python3 online submissions for Fibonacci Number.
