class DomiRow:
    def __init__(self, target: int, turns: int):
        self.target = target
        self.turns = turns
        self.valid = True

    def add(self, same: int, other: int) -> None:
        if not self.valid:
            return

        if same == self.target:
            pass
        elif other == self.target:
            self.turns += 1
        else:
            self.valid = False


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        dominoes = [
            DomiRow(tops[0], turns=0),
            DomiRow(tops[0], turns=1),
            DomiRow(bottoms[0], turns=0),
            DomiRow(bottoms[0], turns=1),
        ]

        for i in range(1, len(tops)):
            top = tops[i]
            bot = bottoms[i]

            dominoes[0].add(top, bot)
            dominoes[1].add(bot, top)
            dominoes[2].add(bot, top)
            dominoes[3].add(top, bot)

        turns = [d.turns for d in dominoes if d.valid]
        if not turns:
            return -1
        return min(turns)


# Runtime: 1356 ms, faster than 63.10% of Python3 online submissions for Minimum Domino Rotations For Equal Row.
# Memory Usage: 15.2 MB, less than 44.98% of Python3 online submissions for Minimum Domino Rotations For Equal Row.
