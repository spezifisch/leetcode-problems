class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        ans = []
        num = 0

        for bit in A:
            if bit == 1:
                num |= 1

            if num % 5 == 0:
                divisible = True
            else:
                divisible = False

            ans.append(divisible)

            num <<= 1

        return ans


# Runtime: 296 ms, faster than 75.00% of Python3 online submissions for Binary Prefix Divisible By 5.
# Memory Usage: 16.2 MB, less than 100.00% of Python3 online submissions for Binary Prefix Divisible By 5.
