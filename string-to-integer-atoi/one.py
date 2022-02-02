class Solution:
    def myAtoi(self, str: str) -> int:
        num = ""

        str = str.strip(" ")
        if not len(str):
            return 0
        if str[0] == "-":
            num += str[0]
            str = str[1:]
        elif str[0] == "+":
            str = str[1:]

        o0 = ord("0")
        o9 = ord("9")
        for c in str:
            if ord(c) >= o0 and ord(c) <= o9:
                num += c
            else:
                break

        try:
            inum = int(num)
        except ValueError:
            return 0

        lim = 2**31
        if inum > lim - 1:
            return lim - 1
        elif inum < -lim:
            return -lim

        return inum


# Runtime: 60 ms, faster than 74.89% of Python3 online submissions for String to Integer (atoi).
# Memory Usage: 13.2 MB, less than 5.00% of Python3 online submissions for String to Integer (atoi).
