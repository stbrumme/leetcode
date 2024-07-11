class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        size = len(floor)

        # our own more efficient cache, because @cache is too memory hungry
        cache = [ [ -1 ] * size for _ in range(numCarpets + 1) ]

        def deeper(pos, carpets):
            if pos >= size:
                return 0

            # memoized
            done = cache[carpets][pos]
            if done > -1:
                return done

            # no need for a carpet
            if floor[pos] == "0":
                return deeper(pos + 1, carpets)

            # no more carpets
            if carpets == 0:
                return floor[pos :].count("1")

            # cover current white tile
            best = deeper(pos + carpetLen, carpets - 1)
            # or leave it open
            best = min(best, 1 + deeper(pos + 1, carpets))

            cache[carpets][pos] = best
            return best

        return deeper(0, numCarpets)
