class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        width  = len(grid[0])
        height = len(grid)

        result = 0
        for y in range(height):
            for x in range(width):
                if grid[y][x] == 1: # land
                    if x == 0 or grid[y][x-1] == 0:
                        result += 1
                    if y == 0 or grid[y-1][x] == 0:
                        result += 1
                    if x == width-1  or grid[y][x+1] == 0:
                        result += 1
                    if y == height-1 or grid[y+1][x] == 0:
                        result += 1

        return result
