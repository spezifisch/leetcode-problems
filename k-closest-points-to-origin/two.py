class Node:
    def __init__(self, point: List[int]):
        self.point = point
        self.val = point[0] ** 2 + point[1] ** 2

    def __str__(self) -> str:
        return f"Point{self.point} val={self.val}"


class MinPQ:
    def __init__(self):
        self.nodes = [0]

    def __str__(self) -> str:
        ret = ""
        for i in range(1, len(self.nodes)):
            ret += f"{i}: {self.nodes[i]}\n"
        return ret.strip("\n")

    def is_valid(self, i: int) -> bool:
        return 1 <= i <= len(self.nodes) - 1

    @staticmethod
    def is_root(i: int) -> bool:
        return i == 1

    def get_parent(self, i: int) -> int:
        pid = i // 2
        return pid, self.nodes[pid]

    @staticmethod
    def get_children(i: int) -> int:
        return 2 * i, 2 * i + 1

    def get_node_safe(self, node_id: int) -> Node:
        if self.is_valid(node_id):
            return self.nodes[node_id]
        return None

    def add(self, node: Node):
        self.nodes.append(node)
        self.swim(len(self.nodes) - 1)

    def pop_min(self) -> Node:
        last_id = len(self.nodes) - 1
        if not self.is_valid(last_id):
            return None

        # min. node is id=1, swap it with the last node
        self.swap(1, last_id)
        # now remove the last node, which is the min.
        min_node = self.nodes.pop(last_id)

        self.sink(1)
        return min_node

    def swap(self, a: int, b: int):
        tmp = self.nodes[a]
        self.nodes[a] = self.nodes[b]
        self.nodes[b] = tmp

    def swim(self, node_id: int):
        if self.is_root(node_id):
            return

        parent_id, parent = self.get_parent(node_id)
        if parent.val > self.nodes[node_id].val:
            self.swap(parent_id, node_id)
            self.swim(parent_id)

    def sink(self, node_id: int):
        if not self.is_valid(node_id):
            return

        me = self.nodes[node_id]
        child_a_id, child_b_id = self.get_children(node_id)
        child_a = self.get_node_safe(child_a_id)
        child_b = self.get_node_safe(child_b_id)

        if child_a and child_b:
            if me.val > child_a.val or me.val > child_b.val:
                if child_a.val < child_b.val:
                    self.swap(node_id, child_a_id)
                    self.sink(child_a_id)
                else:
                    self.swap(node_id, child_b_id)
                    self.sink(child_b_id)
        elif child_a:
            if me.val > child_a.val:
                self.swap(node_id, child_a_id)
                self.sink(child_a_id)
        elif child_b:
            if me.val > child_b.val:
                self.swap(node_id, child_b_id)
                self.sink(child_b_id)


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        pq = MinPQ()

        for point in points:
            node = Node(point)
            pq.add(node)

        # print(pq)

        ret = []
        for i in range(K):
            node = pq.pop_min()

            # print("--")
            # print(pq)

            if not node:
                break

            ret.append(node.point)

        return ret


# Runtime: 2076 ms, faster than 5.03% of Python3 online submissions for K Closest Points to Origin.
# Memory Usage: 18.7 MB, less than 5.20% of Python3 online submissions for K Closest Points to Origin
