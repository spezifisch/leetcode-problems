class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        for i, a in enumerate(nums):
            for j, b in enumerate(nums[i + 1 :]):
                wanted = -(a + b)
                if wanted in nums:
                    triplet = sorted([a, b, wanted])

                    if triplet[0] == triplet[1] or triplet[1] == triplet[2]:
                        nums_count = nums.count(triplet[1])
                        triplet_count = triplet.count(triplet[1])
                        if triplet_count > nums_count:
                            continue

                    if triplet not in ret:
                        ret.append(triplet)

        return ret


# Time Limit Exceeded
