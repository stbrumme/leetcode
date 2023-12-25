class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        size = len(grid)
        for y in range(size - 2):
            for x in range(size - 2):
                grid[y][x] = max(grid[y    ][x], grid[y    ][x + 1], grid[y    ][x + 2], \
                                 grid[y + 1][x], grid[y + 1][x + 1], grid[y + 1][x + 2], \
                                 grid[y + 2][x], grid[y + 2][x + 1], grid[y + 2][x + 2])
            grid[y].pop()
            grid[y].pop()
        grid.pop()
        grid.pop()
        return grid
