class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        @cache
        def deeper(x, y):  # analyze path in reverse: from bottom-right to upper-left
            value = grid[y][x]
            if x == 0 and y == 0:
                return [ value, value ]
            if value == 0: # actually there is no need to handle this edge case ...
                return [ 0, 0 ]

            high = -inf
            low  = +inf

            if x > 0: # go left
                h, l = deeper(x - 1, y)
                h   *= value
                l   *= value
                high, low = max(high, h, l), min(low, h, l)

            if y > 0: # go up
                h, l = deeper(x, y - 1)
                h   *= value
                l   *= value
                high, low = max(high, h, l), min(low, h, l)

            # if value is negative, then high and low must be swapped
            return [ high, low ]

        height = len(grid)
        width  = len(grid[0])

        high, low = deeper(width - 1, height - 1)
        return high % 1_000_000_007 if high >= 0 else -1
