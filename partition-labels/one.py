class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        parts = []
        current_part = []

        for i, c in enumerate(S):
            elements_left = i != len(S) - 1

            if not len(current_part) or c in current_part:
                current_part.append(c)
            elif elements_left and len(set(current_part) & set(S[i + 1 :])):
                current_part.append(c)
            elif elements_left and c not in S[i + 1 :]:
                if c not in current_part:
                    parts.append(len(current_part))
                    current_part = [c]
                else:
                    current_part.append(c)
            else:
                parts.append(len(current_part))
                current_part = [c]

        if len(current_part):
            parts.append(len(current_part))

        return parts


# Runtime: 56 ms, faster than 43.11% of Python3 online submissions for Partition Labels.
# Memory Usage: 13 MB, less than 5.71% of Python3 online submissions for Partition Labels.
