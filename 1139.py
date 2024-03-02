class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        result = 0
        width  = len(grid[0])
        height = len(grid)

        # number of consecutive 1s
        horizontal = []
        vertical   = []
        for y in range(height):
            horizontal.append([ 0 ] * width)
            vertical  .append([ 0 ] * width)
            have = 0
            for x in range(width):
                have += grid[y][x]
                have *= grid[y][x]
                horizontal[y][x] = have

        for x in range(width):
            have = 0
            for y in range(height):
                have += grid[y][x]
                have *= grid[y][x]
                vertical[y][x] = have

        # not a single 1
        total = 0
        for y in range(height):
            total += sum(horizontal[y])
        if total == 0:
            return 0

        largest = min(height, width)
        for y in range(height):
            for x in range(width):
                for side in range(result + 1, largest + 1):
                    x2 = x + side - 1
                    y2 = y + side - 1

                    # right
                    if x2 >= width  or horizontal[y][x2] < side:
                        break
                    # down
                    if y2 >= height or vertical  [y2][x] < side:
                        break
                    # down + right
                    if horizontal[y2][x2] >= side and vertical[y2][x2] >= side:
                        result = max(result, side)

        return result ** 2
