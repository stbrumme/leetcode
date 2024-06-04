class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        horizontal = defaultdict(int)
        vertical   = defaultdict(int)
        diagonals1 = defaultdict(int) # top-left  => bottom-right
        diagonals2 = defaultdict(int) # top-right => bottom-left

        # turn on all (unique) lamps
        lamps = set(( y, x ) for y, x in lamps)
        for y, x in lamps:
            horizontal[y]     += 1
            vertical[x]       += 1
            diagonals1[y - x] += 1
            diagonals2[y + x] += 1

        for y, x in queries:
            result = horizontal[y] + vertical[x] + diagonals1[y - x] + diagonals2[y + x]
            yield 1 if result > 0 else 0

            # turn off up to 9 lights
            for yy in range(y - 1, y + 1 + 1):
                for xx in range(x - 1, x + 1 + 1):
                    if ( yy, xx ) in lamps:
                        lamps.discard(( yy, xx ))
                        if  horizontal[yy]       > 0:
                            horizontal[yy]      -= 1
                        if  vertical[xx]         > 0:
                            vertical[xx]        -= 1
                        if  diagonals1[yy - xx]  > 0:
                            diagonals1[yy - xx] -= 1
                        if  diagonals2[yy + xx]  > 0:
                            diagonals2[yy + xx] -= 1
