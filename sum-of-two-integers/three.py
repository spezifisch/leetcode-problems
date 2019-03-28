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
        mask = 0xffffffff
        a = a & mask
        b = b & mask
        
        result = []
        carry = False
        while a or b:
            carry, bit = self.fullAdder(a & 1 != 0, b & 1 != 0, carry)
            result.append(bit)
            
            a >>= 1
            b >>= 1
            
        result.append(carry)
        
        result_s = "".join(map(lambda b: "1" if b else "0", result[:32][::-1]))
        result_i = unpack("i", pack("I", int(result_s, 2)))
        return result_i[0]
    
# Runtime: 36 ms, faster than 62.82% of Python3 online submissions for Sum of Two Integers.
# Memory Usage: 13.1 MB, less than 5.97% of Python3 online submissions for Sum of Two Integers.

