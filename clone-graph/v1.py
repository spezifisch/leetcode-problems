"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def dfs(self, parent: "Node") -> "Node":
        if parent.val in self.node_map:
            return self.node_map[parent.val]

        self.node_map[parent.val] = Node(parent.val)

        for child in parent.neighbors:
            child_copy = self.dfs(child)
            self.node_map[parent.val].neighbors.append(child_copy)

        return self.node_map[parent.val]

    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None

        self.node_map = {}
        return self.dfs(node)
