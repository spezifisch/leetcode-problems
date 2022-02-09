class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        counter = {}
        for val in nums:
            counter[val] = counter.get(val, 0) + 1

        pairs = 0
        for val in set(nums):
            n = val - k
            if k > 0:
                if n in counter:
                    pairs += 1
            else:
                if counter[val] > 1:
                    pairs += 1

        return pairs


# Runtime: 118 ms, faster than 42.97% of Python3 online submissions for K-diff Pairs in an Array.
# Memory Usage: 16.2 MB, less than 31.62% of Python3 online submissions for K-diff Pairs in an Array.
