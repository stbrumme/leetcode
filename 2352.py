class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        result = 0

        rows = defaultdict(int)
        for g in grid:
            rows[tuple(g)] += 1

        for x in range(n):
            current = [ grid[y][x] for y in range(n) ]
            result += rows[tuple(current)]

        return result
