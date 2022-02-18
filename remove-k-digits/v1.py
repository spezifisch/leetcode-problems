class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for n in num:
            while k > 0 and stack and stack[-1] > n:
                stack.pop()
                k -= 1

            stack.append(n)

        while k > 0:
            stack.pop()
            k -= 1

        num = "".join(stack)
        num = num.lstrip("0")

        if not num:
            num = "0"
        return num


# Runtime: 28 ms, faster than 99.72% of Python3 online submissions for Remove K Digits.
# Memory Usage: 14.1 MB, less than 93.92% of Python3 online submissions for Remove K Digits.
