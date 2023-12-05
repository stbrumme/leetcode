class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        width  = len(grid[0])
        height = len(grid)

        result = [ [ None ] * width for y in range(height)]

        # brute force
        for y in range(height):
            for x in range(width):
                a  = set()
                ax = x
                ay = y
                while ax > 0 and ay > 0:
                    ax -= 1
                    ay -= 1
                    a.add(grid[ay][ax])

                b  = set()
                bx = x
                by = y
                while bx < width - 1 and by < height - 1:
                    bx += 1
                    by += 1
                    b.add(grid[by][bx])

                result[y][x] = abs(len(a) - len(b))

        return result
