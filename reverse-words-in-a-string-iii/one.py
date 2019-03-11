class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([word[::-1] for word in s.split(" ")])
    
# Runtime: 40 ms, faster than 74.73% of Python3 online submissions for Reverse Words in a String III.
# Memory Usage: 13.5 MB, less than 5.70% of Python3 online submissions for Reverse Words in a String III.

