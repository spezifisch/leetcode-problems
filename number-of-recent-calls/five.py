from collections import deque

class RecentCounter:
    def __init__(self):
        self.ping_log = deque()
        self.ping_len = 0

    def ping(self, t: int) -> int:
        self.ping_log.append(t)
        self.ping_len += 1
        
        t_limit = t - 3000
        while True:
            try:
                elem = self.ping_log[0]
            except IndexError:
                break
                
            if elem < t_limit:
                self.ping_log.popleft()
                self.ping_len -= 1
            else:
                break
            
        return self.ping_len

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

# Runtime: 224 ms, faster than 49.90% of Python3 online submissions for Number of Recent Calls.
# Memory Usage: 17.7 MB, less than 5.71% of Python3 online submissions for Number of Recent Calls.

