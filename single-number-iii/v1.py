def get_lowest_one_bit(val: int) -> int:
    for i in range(32):
        if val & (1<<i):
            return i

    raise Exception("no 1 bits")


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_all = 0
        for num in nums:
            xor_all ^= num

        lowest_one_bit = get_lowest_one_bit(xor_all)

        xor_ones = 0
        for num in nums:
            if num & (1<<lowest_one_bit):
                xor_ones ^= num

        a = xor_ones
        b = xor_all ^ xor_ones
        return [a, b]

# Runtime: 56 ms, faster than 91.44% of Python3 online submissions for Single Number III.
# Memory Usage: 15.6 MB, less than 99.27% of Python3 online submissions for Single Number III.

