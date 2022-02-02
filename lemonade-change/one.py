class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = [0, 0]
        for bill in bills:
            if bill == 5:
                change[0] += 1
            elif bill == 10:
                change[1] += 1
                change[0] -= 1
                if change[0] < 0:
                    return False
            elif bill == 20:
                left = 3
                if change[1] > 0:
                    change[1] -= 1
                    left -= 2

                change[0] -= left
                if change[0] < 0:
                    return False
            else:
                assert False

        return True


# Runtime: 52 ms, faster than 65.50% of Python3 online submissions for Lemonade Change.
# Memory Usage: 13.2 MB, less than 6.15% of Python3 online submissions for Lemonade Change.
