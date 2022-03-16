class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        push_idx = 0
        stack = []
        for pop_val in popped:
            if stack and pop_val == stack[-1]:
                stack.pop()
            else:
                found = False
                while not found and push_idx < len(pushed):
                    push_val = pushed[push_idx]
                    if push_val == pop_val:
                        found = True
                    else:
                        stack.append(push_val)

                    push_idx += 1

                if not found:
                    return False

        return True


# Runtime: 95 ms, faster than 60.94% of Python3 online submissions for Validate Stack Sequences.
# Memory Usage: 14.1 MB, less than 63.80% of Python3 online submissions for Validate Stack Sequences.
