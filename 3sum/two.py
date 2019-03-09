def bisect_in(a, x, lo, hi):
    while lo < hi:
        mid = (lo+hi)//2
        if a[mid] < x:
            lo = mid+1
        elif a[mid] > x:
            hi = mid
        else:
            return True
        
    return False

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        nums_len = len(nums)
        ret = set()
        for i in range(nums_len):
            for j in range(i+1, nums_len):
                a = nums[i]
                b = nums[j]
                c = -(a + b)
                if bisect_in(nums, c, lo=j+1, hi=nums_len):
                    triplet = (a, b, c)
                    ret.add(triplet)
        
        return list(ret)
                    
# Runtime: 9648 ms, faster than 5.02% of Python3 online submissions for 3Sum.
# Memory Usage: 17.1 MB, less than 14.58% of Python3 online submissions for 3Sum.

