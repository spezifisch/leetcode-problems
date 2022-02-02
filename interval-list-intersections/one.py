# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

from typing import Tuple


class Solution:
    @staticmethod
    def getNextInterval(L: List[Interval]) -> Tuple[int, bool]:
        for interval in L:
            yield interval.start, True
            yield interval.end, False

        yield None, None

    @staticmethod
    def getNextThing(A: List[Interval], B: List[Interval]) -> Tuple[int, bool, bool]:
        gen_A = Solution.getNextInterval(A)
        gen_B = Solution.getNextInterval(B)
        na_num, na_start = next(gen_A)
        nb_num, nb_start = next(gen_B)

        while na_num is not None or nb_num is not None:
            if (
                na_num is not None
                and nb_num is not None
                and (na_num < nb_num or (na_num == nb_num and na_start))
            ) or nb_num is None:  # sorry for this
                yield na_num, na_start, True
                na_num, na_start = next(gen_A)
            elif nb_num is not None:
                yield nb_num, nb_start, False
                nb_num, nb_start = next(gen_B)

    def intervalIntersection(
        self, A: List[Interval], B: List[Interval]
    ) -> List[Interval]:
        A_open = B_open = False
        new_interval = None
        ret = []

        for num, is_start, is_A in self.getNextThing(A, B):
            if is_A:
                A_open = is_start
            else:
                B_open = is_start

            if A_open and B_open:
                new_interval = [num, None]
            elif new_interval is not None:
                new_interval[1] = num
                ret.append(new_interval)
                new_interval = None

        return ret


# Runtime: 120 ms, faster than 23.14% of Python3 online submissions for Interval List Intersections.
# Memory Usage: 14.3 MB, less than 5.55% of Python3 online submissions for Interval List Intersections.
