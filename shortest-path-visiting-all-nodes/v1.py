from collections import deque


class Visited:
    def __init__(self, *, length: int = 0, other: Optional["Visited"] = None):
        if other is not None:
            self.val = [x for x in other.val]
        else:
            self.val = [False] * length

    def all_set(self) -> bool:
        return all(self.val)

    def set_idx(self, idx: int) -> None:
        self.val[idx] = True

    def is_set(self, idx: int) -> bool:
        return self.val[idx]

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Visited):
            return NotImplemented

        return self.val == other.val

    def __hash__(self) -> int:
        # ugh...
        s = 0
        for i, x in enumerate(self.val):
            if x:
                s += 2**i

        return s


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        visited = set()
        q = deque()

        for start_node in range(len(graph)):
            v = Visited(length=len(graph))
            v.set_idx(start_node)
            q.append((start_node, 0, v))
            visited.add((start_node, v))

        while len(q):
            node_idx, dist, v = q.popleft()

            if v.all_set():
                return dist

            neighbors = graph[node_idx]
            for neighbor_idx in neighbors:
                nv = Visited(other=v)
                nv.set_idx(neighbor_idx)

                key = (neighbor_idx, nv)
                if key not in visited:
                    visited.add(key)
                    q.append((neighbor_idx, dist + 1, nv))

        return -1


# Runtime: 4228 ms, faster than 5.14% of Python3 online submissions for Shortest Path Visiting All Nodes.
# Memory Usage: 26.9 MB, less than 19.35% of Python3 online submissions for Shortest Path Visiting All Nodes.
