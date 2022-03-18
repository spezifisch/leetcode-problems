class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        for i, c in enumerate(s):
            if c not in stack:
                while stack and stack[-1] > c:
                    if stack[-1] not in s[i + 1 :]:
                        break

                    stack.pop()

                stack.append(c)

        return "".join(stack)


# Runtime: 44 ms, faster than 74.60% of Python3 online submissions for Remove Duplicate Letters.
# Memory Usage: 13.9 MB, less than 87.68% of Python3 online submissions for Remove Duplicate Letters.
