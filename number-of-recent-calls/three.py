class RecentCounter:
    def __init__(self):
        self.ping_log = []
        self.ping_len = 0

    def ping(self, t: int) -> int:
        self.ping_log.append(t)
        self.ping_len += 1

        t_delete_before = None
        t_limit = t - 3000
        for i, t_old in enumerate(self.ping_log[::-1]):
            if t_old < t_limit:
                t_delete_before = self.ping_len - 1 - i
                break

        if t_delete_before is not None:
            del self.ping_log[: t_delete_before + 1]
            self.ping_len -= t_delete_before + 1

        return self.ping_len


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

# Runtime: 3148 ms, faster than 7.31% of Python3 online submissions for Number of Recent Calls.
# Memory Usage: 17.8 MB, less than 5.71% of Python3 online submissions for Number of Recent Calls.
