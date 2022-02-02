from typing import Tuple
from struct import pack, unpack


class Solution:
    @staticmethod
    def halfAdder(a: bool, b: bool) -> Tuple[bool, bool]:
        sm = a != b
        carry = a and b
        return (carry, sm)

    @staticmethod
    def fullAdder(a: bool, b: bool, cin: bool) -> Tuple[bool, bool]:
        c_ab, sm_ab = Solution.halfAdder(a, b)
        c_abc, sm_abc = Solution.halfAdder(sm_ab, cin)
        cout = c_ab != c_abc
        return (cout, sm_abc)

    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        a = a & mask
        b = b & mask

        result = []
        carry = False
        while a or b:
            carry, bit = self.fullAdder(a & 1, b & 1, carry)
            result.append(bit)

            a >>= 1
            b >>= 1

        result.append(carry)

        result_uint = 0
        for i in range(min(32, len(result))):
            if result[i]:
                result_uint |= 1 << i

        (result_int,) = unpack("i", pack("I", result_uint))
        return result_int


# Runtime: 36 ms, faster than 62.82% of Python3 online submissions for Sum of Two Integers.
# Memory Usage: 13.3 MB, less than 5.97% of Python3 online submissions for Sum of Two Integers.
