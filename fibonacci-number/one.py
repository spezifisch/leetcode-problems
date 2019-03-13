class Solution:
    def __init__(self):
        self.cache = {
            0: 0,
            1: 1,
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

