class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) - 1
        border_left = border_right = None

        while i <= j and border_left is None and border_right is None:
            if nums[i] != target:
                i += 1
            else:
                # found left border
                border_left = i

            if nums[j] != target:
                j -= 1
            else:
                # found right border
                border_right = j

        if border_left is None and border_right is None:
            return [-1, -1]
        elif border_left is not None and border_right is not None:
            pass
        elif border_left is None:
            border_left = i + nums[i : j + 1].index(target)
        else:
            lower = i - 1
            if lower < 0:
                lower = None
            border_right = j + 1 - nums[j + 1 : lower : -1].index(target)

        return [border_left, border_right]


# Runtime: 56 ms, faster than 24.18% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
# Memory Usage: 14 MB, less than 5.06% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
