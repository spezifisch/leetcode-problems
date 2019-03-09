class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = 0
        y = 0
        for move in moves:
            if move == 'U':
                y += 1
            elif move == 'D':
                y -= 1
            elif move == 'R':
                x += 1
            elif move == 'L':
                x -= 1
        
        return x == 0 and y == 0
    
# Runtime: 68 ms, faster than 48.44% of Python3 online submissions for Robot Return to Origin.
# Memory Usage: 13.2 MB, less than 5.32% of Python3 online submissions for Robot Return to Origin.

