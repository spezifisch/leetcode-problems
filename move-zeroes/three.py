class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroes = 0
        pos = 0
        while pos < len(nums):
            if nums[pos] == 0:
                del nums[pos]
                zeroes += 1
            else:
                pos += 1

        nums += [0] * zeroes


# Runtime: 52 ms, faster than 53.18% of Python3 online submissions for Move Zeroes.
# Memory Usage: 14.4 MB, less than 5.21% of Python3 online submissions for Move Zeroes.
