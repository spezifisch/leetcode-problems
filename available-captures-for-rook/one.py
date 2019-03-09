class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        rook_pos = None
        for row in range(len(board)):
            for col in range(len(board)):
                elem = board[row][col]
                if elem == 'R':
                    rook_pos = (row, col)
                    break
                   
        pawns = 0
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        for direction in dirs:
            pos = rook_pos
            while True:
                pos = list(map(sum, zip(pos, direction)))
                if pos[0] < 0 or pos[0] >= len(board):
                    break
                if pos[1] < 0 or pos[1] >= len(board):
                    break
                    
                elem = board[pos[0]][pos[1]]
                if elem == 'B':
                    break
                if elem == 'p':
                    pawns += 1
                    break
                    
        return pawns
                    
# Runtime: 36 ms, faster than 99.75% of Python3 online submissions for Available Captures for Rook.
# Memory Usage: 13.1 MB, less than 100.00% of Python3 online submissions for Available Captures for Rook.

