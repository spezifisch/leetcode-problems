class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        board_len = 8
        rook_pos = None

        # previous element in rook's row
        prev_in_row = None
        # next one
        next_in_row = None
        # save which non-empty element was encountered last in every column
        # until we find the rook
        prev_in_every_col = ["."] * len(board)

        for row in range(board_len):
            # reset for every row
            prev_in_row = None
            next_in_row = None

            for col in range(board_len):
                elem = board[row][col]
                if not rook_pos and elem == "R":
                    rook_pos = (row, col)
                else:
                    # update previous non-empty element in row until we find the rook
                    if not rook_pos:
                        if elem != ".":
                            prev_in_row = elem
                            prev_in_every_col[col] = elem
                    # after we found the rook, look for the next non-empty element
                    if rook_pos and row == rook_pos[0]:
                        if elem != ".":
                            next_in_row = elem
                            break  # stop after this element

            # rook found in this line
            if rook_pos:
                break

        # now that we have the rook position, look which element was previous in his column
        prev_in_col = prev_in_every_col[rook_pos[1]]

        # find next element in rook's column
        next_in_col = None
        for row in range(rook_pos[0] + 1, len(board)):
            elem = board[row][rook_pos[1]]
            if elem != ".":
                next_in_col = elem
                break

        nearest_elems = [prev_in_row, next_in_row, prev_in_col, next_in_col]
        return nearest_elems.count("p")


# Runtime: 36 ms, faster than 99.77% of Python3 online submissions for Available Captures for Rook.
# Memory Usage: 13.3 MB, less than 100.00% of Python3 online submissions for Available Captures for Rook.
