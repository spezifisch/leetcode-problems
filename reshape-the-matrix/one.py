class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if not nums or not nums[0]:
            return nums
        if len(nums) * len(nums[0]) != r * c:
            return nums

        new_mat = [[0] * c for _ in range(r)]
        cell = 0

        for nums_row in nums:
            for nums_cell in nums_row:
                new_mat[cell // c][cell % c] = nums_cell
                cell += 1

        return new_mat


# Runtime: 96 ms, faster than 53.95% of Python3 online submissions for Reshape the Matrix.
# Memory Usage: 14.2 MB, less than 5.66% of Python3 online submissions for Reshape the Matrix.
