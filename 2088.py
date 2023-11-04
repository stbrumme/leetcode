class Solution:
    def countPyramids(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width  = len(grid[0])

        spans = [] # consecutive fertile cells on the left side, including current cell (prefix sum)
        for y in range(height):
            row = []
            count = 0
            for x in range(width):
                if grid[y][x] == 0:
                    count  = 0 # reset
                else:
                    count += 1
                row.append(count)
            spans.append(row)

        result = 0
        for y in range(height):
            for x in range(width):
                # "normal" pyramids (apex at top)
                for i in range(height):
                    dx = x + i
                    dy = y + i
                    if dx >= width or dy >= height:
                        break

                    # expected width of pyramid
                    need = 2 * i + 1
                    if spans[dy][dx] < need:
                        break

                    # at least two cells high
                    if i >= 1:
                        result += 1

                # "inverted" pyramids (apex at bottom)
                # same code but dy goes up instead of down
                for i in range(height):
                    dx = x + i
                    dy = y - i
                    if dx >= width or dy < 0:
                        break

                    # expected width of pyramid
                    need = 2 * i + 1
                    if spans[dy][dx] < need:
                        break

                    # at least two cells high
                    if i >= 1:
                        result += 1

        return result
