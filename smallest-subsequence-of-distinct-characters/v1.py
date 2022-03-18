class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stack = []
        for i, c in enumerate(s):
            if c not in stack:
                while stack and stack[-1] > c:
                    if stack[-1] not in s[i + 1 :]:
                        break

                    stack.pop()

                stack.append(c)

        return "".join(stack)


# Runtime: 36 ms, faster than 81.03% of Python3 online submissions for Smallest Subsequence of Distinct Characters.
# Memory Usage: 13.9 MB, less than 76.77% of Python3 online submissions for Smallest Subsequence of Distinct Characters.
