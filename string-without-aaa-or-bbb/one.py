class Solution:
    def strWithout3a3b(
        self, A: int, B: int, letter: str = "a", other_letter: str = "b"
    ) -> str:
        if not A and not B:
            return ""
        if not A:
            return "b" * B
        if not B:
            return "a" * A

        if A < B:
            return self.strWithout3a3b(B, A, "b", "a")

        ret = []

        while A > 0:
            ret.append(letter)
            A -= 1
            if A > 0:
                ret.append(letter)
                A -= 1
                if A > 0:
                    ret.append(other_letter)
                    B -= 1

        assert B >= 0

        if B > 0:
            if ret[-1] == letter:
                ret.append(other_letter)
                B -= 1
                if B > 0:
                    ret.append(other_letter)
                    B -= 1
            elif ret[-2] == letter:
                ret.append(other_letter)
                B -= 1

        if B > 0:
            ret.insert(0, other_letter)
            B -= 1
            if B > 0:
                ret.insert(0, other_letter)
                B -= 1

        pos = 1
        while pos < len(ret) - 1 and B > 0:
            if ret[pos] != other_letter:
                pos += 1
                continue
            if ret[pos - 1] != letter or ret[pos + 1] != letter:
                pos += 1
                continue

            ret.insert(pos, other_letter)
            B -= 1
            pos += 2

        return "".join(ret)


# Runtime: 36 ms, faster than 71.60% of Python3 online submissions for String Without AAA or BBB.
# Memory Usage: 13.2 MB, less than 5.45% of Python3 online submissions for String Without AAA or BBB.
