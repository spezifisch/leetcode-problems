class Solution:
    NEIGHBORS = ((-1, 0), (1, 0), (0, -1), (0, 1))
    
    def floodFill(self, row, col):
        if self.A[row][col] != 1:
            return
        
        q = list()
        q.append((row, col))
        
        while len(q):
            current_pos = q.pop()
            self.A[current_pos[0]][current_pos[1]] = 5
            
            for neighbor in self.NEIGHBORS:
                pos = (current_pos[0] + neighbor[0], current_pos[1] + neighbor[1])
                if 0 < pos[0] < self.rows-1 and 0 < pos[1] < self.cols-1:
                    if self.A[pos[0]][pos[1]] == 1:
                        q.append(pos)

    def numEnclaves(self, A: List[List[int]]) -> int:
        self.A = A
        
        self.rows = rows = len(A)
        self.cols = cols = len(A[0])
        
        for row in (0, rows-1):
            for col in range(cols):
                if A[row][col] == 1:
                    self.floodFill(row, col)
                
        for col in (0, cols-1):
            for row in range(1, rows-1):
                if A[row][col] == 1:
                    self.floodFill(row, col)
                
        cnt = 0
        for row in range(rows):
            for col in range(cols):
                if A[row][col] == 1:
                    cnt += 1
                    
        return cnt
    
# Runtime: 156 ms, faster than 47.28% of Python3 online submissions for Number of Enclaves.
# Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Number of Enclaves.

