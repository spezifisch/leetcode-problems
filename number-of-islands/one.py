DEBUG = True


class UnionFind:
    def __init__(self, n):
        self.cells = list(range(n))

    def union(self, a, b):
        old_b = self.cells[b]
        new_b = self.cells[a]

        self.cells[b] = new_b

        for i in range(len(self.cells)):
            if self.cells[i] == old_b:
                self.cells[i] = new_b

    def connected(self, a, b):
        return self.cells[a] == self.cells[b]

    def count(self):
        return len(set(self.cells))

    def dump(self, x):
        if not DEBUG:
            return

        stack = self.cells
        while len(stack):
            part = stack[:x]
            stack = stack[x:]
            print(part)


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dim_y = len(grid)
        if not dim_y:
            return 0
        dim_x = len(grid[0])
        if not dim_x:
            return 0

        if DEBUG:
            for y in range(dim_y):
                print("".join(grid[y]))

            print("==")

        water = None
        uf = UnionFind(dim_x * dim_y)
        uf.dump(dim_x)

        for y in range(dim_y):
            for x in range(dim_x):
                cell_id = y * dim_x + x
                cell = grid[y][x]
                if cell == "0":
                    if water is not None:
                        uf.union(water, cell_id)
                    else:
                        water = cell_id
                else:
                    if x < dim_x - 1:
                        next_cell = grid[y][x + 1]
                        next_cell_id = cell_id + 1
                        if next_cell == "1":
                            uf.union(cell_id, next_cell_id)

                    if y < dim_y - 1:
                        next_cell = grid[y + 1][x]
                        next_cell_id = cell_id + dim_x
                        if next_cell == "1":
                            uf.union(cell_id, next_cell_id)

        num_islands = uf.count()
        if water is not None:
            num_islands -= 1

        if DEBUG:
            print("--")
            print("water:", water)
            uf.dump(dim_x)

        return num_islands


# Wrong Answer
