class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        height = len(grid)
        width  = len(grid[0])

        # our own caching since @cache fails
        cache = [ -1 ] * height * width * k
        def linear(x, y, modulo):
            return (y * width + x) * k + modulo

        def deeper(x, y, modulo):
            if x == width or y == height:
                return 0

            # look up cache
            id = linear(x, y, modulo)
            seen = cache[id]
            if seen > -1:
                return seen

            # keep going
            modulo += grid[y][x]
            modulo %= k

            if x == width - 1 and y == height - 1:
                # reached the end
                return 1 if modulo == 0 else 0
            else:
                # need to continue
                result  = deeper(x + 1, y, modulo) + deeper(x, y + 1, modulo)
                result %= 1_000_000_007
                cache[id] = result
                return result

        return deeper(0, 0, 0)
