class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroes = 0
        try:
            while True:
                nums.remove(0)
                zeroes += 1
        except ValueError:
            nums += [0] * zeroes
            
# Runtime: 100 ms, faster than 21.98% of Python3 online submissions for Move Zeroes.
# Memory Usage: 14.3 MB, less than 5.21% of Python3 online submissions for Move Zeroes.

