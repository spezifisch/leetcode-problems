import copy


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_chars = {}
        for c in s1:
            s1_chars[c] = s1_chars.get(c, 0) + 1

        s1_copy = copy.deepcopy(s1_chars)
        current_slice = []
        for c in s2:
            if c not in s1_copy:
                if current_slice and current_slice[0] == c:
                    current_slice.pop(0)
                    current_slice.append(c)
                else:
                    s1_copy = copy.deepcopy(s1_chars)
                    current_slice = []

            if c in s1_copy:
                current_slice.append(c)
                if s1_copy[c] == 1:
                    del s1_copy[c]

                    if not s1_copy:
                        return True
                else:
                    s1_copy[c] -= 1

        return False


# Wrong Answer
