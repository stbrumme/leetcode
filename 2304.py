class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        height = len(grid)
        width  = len(grid[0])

        previous = grid[0] # first row
        for y in range(height - 1):
            next = [ +inf ] * width

            for x in range(width):
                id = grid[y][x]
                for x2 in range(width):
                    # try all paths between two consecutive rows
                    cost = previous[x] + moveCost[id][x2] + grid[y + 1][x2]
                    next[x2] = min(next[x2], cost)
            previous = next

        return min(previous)
