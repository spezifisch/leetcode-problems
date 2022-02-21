class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm
        vote = None
        count = None
        for num in nums:
            if vote is None:
                count = 1
                vote = num
            elif vote == num:
                count += 1
            else:
                count -= 1

                if count == 0:
                    vote = num
                    count = 1

        return vote


# Runtime: 197 ms, faster than 61.31% of Python3 online submissions for Majority Element.
# Memory Usage: 15.5 MB, less than 43.74% of Python3 online submissions for Majority Element.
