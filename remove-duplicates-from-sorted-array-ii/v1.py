class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last_val = None
        last_count = None

        len_nums = len(nums)
        removed_count = 0

        for i in range(len_nums):
            val = nums[i]
            if last_val == val:
                last_count += 1
                if last_count > 2:
                    # remove element
                    removed_count += 1
                    continue
            else:
                last_val = val
                last_count = 1

            nums[i - removed_count] = val

        return len_nums - removed_count


# Runtime: 48 ms, faster than 97.23% of Python3 online submissions for Remove Duplicates from Sorted Array II.
# Memory Usage: 13.9 MB, less than 96.82% of Python3 online submissions for Remove Duplicates from Sorted Array II.
