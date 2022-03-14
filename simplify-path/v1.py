class Solution:
    def simplifyPath(self, path: str) -> str:
        stack_in = path.split("/")
        stack_out = []

        for part in stack_in:
            if not part:
                pass
            elif part == ".":
                pass
            elif part == "..":
                if stack_out:
                    stack_out.pop()
            else:
                stack_out.append(part)

        return "/" + "/".join(stack_out)


# Runtime: 45 ms, faster than 58.05% of Python3 online submissions for Simplify Path.
# Memory Usage: 13.9 MB, less than 57.22% of Python3 online submissions for Simplify Path.
