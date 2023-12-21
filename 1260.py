class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        width  = len(grid[0])
        height = len(grid)
        size   = width * height

        # 2D => 1D (zero-based)
        def two2one(x, y):
            return y * width + x

        # 1D => 2D (zero-based)
        def one2two(n):
            x = n %  width
            y = n // width
            return x, y

        # store all values
        all = {}
        for y in range(height):
            for x in range(width):
                all[two2one(x, y)] = grid[y][x]

        # overwrite grid with shifted values
        for y in range(height):
            for x in range(width):
                original = two2one(x, y)
                shifted  = original + k
                shifted %= size
                kx, ky = one2two(shifted)
                grid[ky][kx] = all[original]

        return grid
