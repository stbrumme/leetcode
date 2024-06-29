class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        height = len(grid)
        width  = len(grid[0])

        # ugly code but I wanted to make it as fast as possible

        for y in range(height - 1):
            for a, b in zip(grid[y], grid[y + 1]):
                if a != b:
                    return False

        for row in grid:
            for a, b in zip(row, row[1 : ]):
                if a == b:
                    return False

        return True
