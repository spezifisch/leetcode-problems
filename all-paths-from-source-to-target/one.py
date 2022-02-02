class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.graph = graph
        self.target = len(graph) - 1
        self.paths = []

        self.explore([0])

        return self.paths

    def explore(self, path: List[int]):
        pos = path[-1]
        if pos == self.target:
            self.paths.append(path)
            return

        for neighbor in self.graph[pos]:
            self.explore(path + [neighbor])


# Runtime: 152 ms, faster than 61.01% of Python3 online submissions for All Paths From Source to Target.
# Memory Usage: 14.7 MB, less than 11.36% of Python3 online submissions for All Paths From Source to Target.
