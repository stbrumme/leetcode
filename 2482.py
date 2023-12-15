class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        width  = len(grid[0])
        height = len(grid)

        # count only 1s
        row = [ sum(r) for r in grid ]
        col = [ 0 ] * width
        for i in range(width):
            for j in range(height):
                col[i] += grid[j][i]

        # overwrite grid
        for j in range(height):
            for i in range(width):
                ones = row[j] + col[i]
                zero = (width - row[j]) + (height - col[i])
                grid[j][i] = ones - zero

        return grid
