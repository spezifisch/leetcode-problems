class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        timed = dict.fromkeys(range(60), 0)
        for key in time:
            timed[key % 60] += 1

        count = 0

        for i, val_a in enumerate(time):
            val_a %= 60
            val_b = 60 - val_a
            if val_a == 0:
                val_b = 0
            count += timed[val_b]

            if val_a == val_b:
                count -= 1

        # everything is counted twice (forward and backward tuple)
        return count // 2
