from collections import deque
from itertools import takewhile

class RecentCounter:
    def __init__(self):
        self.ping_log = deque()

    def ping(self, t: int) -> int:
        self.ping_log.appendleft(t)
        t_limit = t - 3000
        self.ping_log = deque(takewhile(lambda t_old: t_old >= t_limit, self.ping_log))
        return len(self.ping_log)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

# Runtime: 5068 ms, faster than 5.07% of Python3 online submissions for Number of Recent Calls.
# Memory Usage: 17.6 MB, less than 5.71% of Python3 online submissions for Number of Recent Calls.

