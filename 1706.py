class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        height = len(grid)
        width  = len(grid[0])

        for i in range(width):
            x = i
            for y in range(height):
                cell = grid[y][x]
                x   += cell
                if x < 0 or x >= width:
                    yield -1 # out of bounds
                    break

                if grid[y][x] != cell:
                    yield -1 # stuck in a "V"
                    break

                if y == height - 1:
                    yield x # reached bottom
