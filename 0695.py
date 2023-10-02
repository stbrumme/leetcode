class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid[0])
        n = len(grid)

        def count(x, y):
            if grid[y][x] != 1:
                return 0

            grid[y][x] = 2 # avoid processing the same island multiple times

            area = 1
            if x > 0:
                area += count(x - 1, y)
            if x < m - 1:
                area += count(x + 1, y)
            if y > 0:
                area += count(x, y - 1)
            if y < n - 1:
                area += count(x, y + 1)
            return area

        result = 0
        for y in range(n):
            for x in range(m):
                if grid[y][x] == 1:
                    result = max(result, count(x, y))
        return result
