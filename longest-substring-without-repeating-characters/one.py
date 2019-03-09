class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        stack = ""
        for c in s:
            if c in stack:
                c_stack_idx = stack.index(c)
                stack = stack[c_stack_idx+1:]
            
            stack += c
            
            if len(stack) > longest:
                longest = len(stack)
            
        return longest

# Runtime: 76 ms, faster than 90.17% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 13.4 MB, less than 5.05% of Python3 online submissions for Longest Substring Without Repeating Characters.

