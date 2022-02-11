import copy


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_chars = {}
        for c in s1:
            s1_chars[c] = s1_chars.get(c, 0) + 1

        for i, start_c in enumerate(s2):
            if i + len(s1) > len(s2):
                break

            if start_c in s1_chars:
                s1_copy = copy.deepcopy(s1_chars)

                for j in range(len(s1)):
                    c = s2[i + j]

                    if c in s1_copy:
                        if s1_copy[c] == 1:
                            del s1_copy[c]

                            if not s1_copy:
                                return True
                        else:
                            s1_copy[c] -= 1
                    else:
                        s1_copy = copy.deepcopy(s1_chars)

        return False


# Time Limit Exceeded
