class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = "".join(sorted(s))
        t = "".join(sorted(t))
        return s == t


# Runtime: 68 ms, faster than 53.75% of Python3 online submissions for Valid Anagram.
# Memory Usage: 14 MB, less than 5.21% of Python3 online submissions for Valid Anagram.
