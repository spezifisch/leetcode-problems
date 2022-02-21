class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm
        threshold = int(len(nums) / 2)
        vote = None
        count = None
        for num in nums:
            if vote is None:
                count = 1
                vote = num
            elif vote == num:
                count += 1

                if count > threshold:
                    return vote
            else:
                count -= 1

                if count == 0:
                    vote = num
                    count = 1

        return vote


# Runtime: 172 ms, faster than 80.55% of Python3 online submissions for Majority Element.
# Memory Usage: 15.5 MB, less than 81.81% of Python3 online submissions for Majority Element.
