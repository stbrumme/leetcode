class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid[0])
        n = len(grid)

        # sink into the water (the true meaning of flood-fill ...)
        def sink(x, y):
            if grid[y][x] != 1:
                return

            grid[y][x] = 0

            if x > 0:
                sink(x - 1, y)
            if x < m - 1:
                sink(x + 1, y)
            if y > 0:
                sink(x, y - 1)
            if y < n - 1:
                sink(x, y + 1)

        # convert islands on the boundary to water
        for x in range(m):
            if grid[0][x] != 0:
                sink(x, 0)
            if grid[n - 1][x] != 0:
                sink(x, n - 1)
        for y in range(n):
            if grid[y][0] != 0:
                sink(0, y)
            if grid[y][m - 1] != 0:
                sink(m - 1, y)

        # what's still left ?
        found = 0
        for y in range(1, n - 1):
            for x in range(1, m - 1):
                found += grid[y][x]

        return found
