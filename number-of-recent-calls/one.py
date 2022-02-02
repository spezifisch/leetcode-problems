class RecentCounter:
    def __init__(self):
        self.ping_log = []

    def ping(self, t: int) -> int:
        self.ping_log.append(t)

        t_delete_before = None
        for i, t_old in enumerate(self.ping_log[::-1]):
            if t_old < t - 3000:
                t_delete_before = len(self.ping_log) - 1 - i
                break

        if t_delete_before is not None:
            self.ping_log = self.ping_log[t_delete_before + 1 :]

        return len(self.ping_log)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

# Runtime: 4412 ms, faster than 5.26% of Python3 online submissions for Number of Recent Calls.
# Memory Usage: 18 MB, less than 5.71% of Python3 online submissions for Number of Recent Calls.
