class Solution:
    def romanToInt(self, s: str) -> int:
        table = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        stup = [table[k] for k in s[::-1]]
        val = 0
        biggest = 0

        for place in stup:
            if place >= biggest:
                val += place
                biggest = place
            else:
                val -= place

        return val


# Runtime: 132 ms, faster than 64.37% of Python3 online submissions for Roman to Integer.
# Memory Usage: 13.5 MB, less than 5.05% of Python3 online submissions for Roman to Integer.
