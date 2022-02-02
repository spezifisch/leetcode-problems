class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = [
            set("qwertyuiop"),
            set("asdfghjkl"),
            set("zxcvbnm"),
        ]

        possible = []
        for word in words:
            lwordset = set(word.lower())
            for row in rows:
                if lwordset == (lwordset & row):
                    possible.append(word)
                    break

        return possible


# Runtime: 36 ms, faster than 57.57% of Python3 online submissions for Keyboard Row.
# Memory Usage: 13.1 MB, less than 6.58% of Python3 online submissions for Keyboard Row.
