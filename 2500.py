class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width  = len(grid[0])

        for i in range(height):
            grid[i].sort()

        return sum(max(grid[i].pop() for i in range(height)) for j in range(width))
