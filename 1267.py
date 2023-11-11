class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        width  = len(grid[0])
        height = len(grid)

        rows = defaultdict(int)
        cols = defaultdict(int)
        for y in range(height):
            for x in range(width):
                cols[x] += grid[y][x]
                rows[y] += grid[y][x]

        result = 0
        for y in range(height):
            for x in range(width):
                if grid[y][x] == 1 and (cols[x] > 1 or rows[y] > 1):
                    result += 1
        return result
