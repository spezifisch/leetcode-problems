class Solution:
    def combinationSum(
        self, candidates: List[int], target: int, recursed: bool = False
    ) -> List[List[int]]:
        if not recursed:
            candidates.sort()
            candidates.reverse()

        if target <= 0:
            return []

        ret = []

        for i, num in enumerate(candidates):
            if num > target:
                pass
            else:
                added = None
                if (target % num) == 0:
                    added = [num] * (target // num)
                    ret.append(added)

                remainder = candidates[i + 1 :]
                if len(remainder) >= 1:
                    child_target = target - num
                    num_multiple = 0

                    while child_target > 0:
                        child_combis = self.combinationSum(
                            remainder, child_target, recursed=True
                        )
                        child_target -= num
                        num_multiple += 1

                        for combi in child_combis:
                            ret.append([num] * num_multiple + combi)
                else:
                    my_sum = 0
                    num_multiple = 0

                    while my_sum <= target:
                        num_multiple += 1
                        my_sum += num

                        if target == my_sum:
                            cand = [num] * num_multiple
                            if added is None or added != cand:
                                ret.append(cand)
                            break

        return ret


# Runtime: 68 ms, faster than 83.26% of Python3 online submissions for Combination Sum.
# Memory Usage: 13.4 MB, less than 5.14% of Python3 online submissions for Combination Sum.
