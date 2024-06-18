class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        height = len(grid)
        width  = len(grid[0])
        modulo = 12345

        # the 2D case is actually identical to the 1D case
        # I kind of flatten the grid and multiply all numbers from the left and from the right

        left   = []
        total  = 1
        for y in range(height):
            for x in range(width):
                left.append(total)
                total *= grid[y][x]
                total %= modulo

        right  = []
        total  = 1
        for y in reversed(range(height)):
            for x in reversed(range(width)):
                right.append(total)
                total *= grid[y][x]
                total %= modulo

        # join left and right side
        both = zip(left, reversed(right))
        for y in range(height):
            for x in range(width):
                l, r = next(both)
                grid[y][x] = (l * r) % modulo

        return grid
