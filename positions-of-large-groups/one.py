class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        last_char_idx = len(S) - 1
        large = []
        group_char = None
        group_size = 0
        for i, c in enumerate(S):
            if c != group_char:
                if group_size >= 3:
                    large.append([i - group_size, i - 1])

                group_char = c
                group_size = 1
            else:
                group_size += 1

                if i == last_char_idx and group_size >= 3:
                    large.append([i - group_size + 1, i])

        return large


# Runtime: 48 ms, faster than 93.31% of Python3 online submissions for Positions of Large Groups.
# Memory Usage: 13.1 MB, less than 6.98% of Python3 online submissions for Positions of Large Groups.
