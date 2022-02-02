class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        char_counts = [widths[ord(c) - ord("a")] for c in S]

        last_line_width = 0
        lines = 0
        offset = 0
        while offset < len(char_counts):
            line_elements = 0
            line_width = 0
            for cc in char_counts[offset:]:
                if line_width + cc > 100:
                    break

                line_width += cc
                line_elements += 1

            last_line_width = line_width
            lines += 1
            offset += line_elements

        return [lines, last_line_width]


# Runtime: 40 ms, faster than 46.41% of Python3 online submissions for Number of Lines To Write String.
# Memory Usage: 12.9 MB, less than 7.14% of Python3 online submissions for Number of Lines To Write String.
