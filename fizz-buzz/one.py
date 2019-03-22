class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ret = [str(x) for x in range(1, n + 1)]
        ret[2::3] = ["Fizz"] * (n // 3)
        ret[4::5] = ["Buzz"] * (n // 5)
        ret[14::15] = ["FizzBuzz"] * (n // 15)
        return ret
    
# Runtime: 56 ms, faster than 60.72% of Python3 online submissions for Fizz Buzz.
# Memory Usage: 14.4 MB, less than 5.17% of Python3 online submissions for Fizz Buzz.

