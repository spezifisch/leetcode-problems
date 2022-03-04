class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        glasses = []
        row = 0
        any_excess = True
        while any_excess and row <= query_row:
            # per glass: (pour_in, pour_excess)
            row_glasses = [(0, 0)] * (row + 1)
            any_excess = False

            for j in range(row + 1):
                pour_excess = 0.0

                if row == 0:
                    pour_in = float(min(1, poured))
                    pour_excess = poured - pour_in
                    row_glasses[0] = (pour_in, pour_excess)
                else:
                    inflow = 0.0
                    # left parent
                    if j != 0:
                        parent_excess = glasses[row - 1][j - 1][1]
                        if parent_excess >= 0.0:
                            inflow += 0.5 * parent_excess

                    # right parent
                    if j != row:
                        parent_excess = glasses[row - 1][j][1]
                        if parent_excess >= 0.0:
                            inflow += 0.5 * parent_excess

                    pour_in = min(1.0, inflow)
                    pour_excess = inflow - pour_in
                    row_glasses[j] = (pour_in, pour_excess)

                if pour_excess > 0.0:
                    any_excess = True

            glasses.append(row_glasses)
            row += 1

        if 0:
            for i, row in enumerate(glasses):
                print(f"{i:3d} {row}")
            print("-" * i)

        try:
            return glasses[query_row][query_glass][0]
        except IndexError:
            return 0.0


# Runtime: 354 ms, faster than 12.62% of Python3 online submissions for Champagne Tower.
# Memory Usage: 14.5 MB, less than 20.39% of Python3 online submissions for Champagne Tower.
