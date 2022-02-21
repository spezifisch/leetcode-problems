class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        last_num = None
        last_count = None
        for num in nums:
            if num != last_num:
                last_num = num
                last_count = 1
            else:
                last_count += 1

            if last_count > len(nums) / 2:
                return last_num

        return -1


# Runtime: 196 ms, faster than 61.77% of Python3 online submissions for Majority Element.
# Memory Usage: 15.5 MB, less than 81.81% of Python3 online submissions for Majority Element.
