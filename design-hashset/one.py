import bisect


class MyHashSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.values = []

    def _get_idx(self, key: int) -> int:
        return bisect.bisect_left(self.values, key)

    def add(self, key: int) -> None:
        idx = self._get_idx(key)
        try:
            if self.values[idx] != key:
                self.values.insert(idx, key)
        except IndexError:
            self.values.append(key)

    def remove(self, key: int) -> None:
        idx = self._get_idx(key)
        try:
            if self.values[idx] == key:
                del self.values[idx]
        except IndexError:
            pass

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        idx = self._get_idx(key)
        return idx < len(self.values) and self.values[idx] == key


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

# Runtime: 148 ms, faster than 65.30% of Python3 online submissions for Design HashSet.
# Memory Usage: 17.1 MB, less than 41.46% of Python3 online submissions for Design HashSet.
