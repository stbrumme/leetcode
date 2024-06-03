class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        result = set()

        height = len(grid)
        width  = len(grid[0])

        # size zero
        for row in grid:
            result.update(row)
        result = sorted(result)[-3 :] # list with three largest distinct sums

        # start with left-most point, then process in clockwise order
        deltas = ( ( +1, -1 ), ( +1, +1), ( -1, +1 ), ( -1, -1 ))
        for sy in range(height):
            for sx in range(width):
                total = 0
                for side in count(1):
                    # out-of-bounds
                    if sy - side < 0 or sy + side >= height or sx + 2*side >= width:
                        break

                    x = sx
                    y = sy
                    total = 0
                    for dx, dy in deltas:
                        for i in range(side):
                            x += dx
                            y += dy
                            total += grid[y][x]

                    if total not in result:
                        insort(result, total)
                        if len(result) > 3:
                            result.pop(0) # remove smallest

        return reversed(result)
