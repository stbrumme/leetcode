class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        width  = len(grid[0])
        height = len(grid)

        result = 0
        for y in range(1, height - 1):
            for x in range(1, width - 1):
                current = grid[y - 1][x - 1] + \
                          grid[y - 1][x    ] + \
                          grid[y - 1][x + 1] + \
                          grid[y    ][x    ] + \
                          grid[y + 1][x - 1] + \
                          grid[y + 1][x    ] + \
                          grid[y + 1][x + 1]
                result = max(result, current)
        return result
