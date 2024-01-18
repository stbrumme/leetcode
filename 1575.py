class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        # use absolute positions instead of city IDs
        start  = locations[start]
        finish = locations[finish]
        # sort cities to allow the use of fast binary search in deeper()
        locations.sort()

        @cache
        def deeper(pos, gas): # ways to reach finish from pos with certain amount of fuel
            if gas < 0:    # out of gas
                return 0

            result = 0
            if pos == finish:
                result = 1 # made it to the finish line ...
                           # but it's possible to drive back to some city and then return to finish
                           # therefore we MUST NOT return 1 at this point

            # determine range
            a = bisect_left (locations, pos - gas)
            b = bisect_right(locations, pos + gas)
            # scan all cities in that range
            for l in locations[a : b]:
                if l != pos:
                    distance = abs(l - pos)
                    result  += deeper(l, gas - distance)

            return result % 1_000_000_007

        return deeper(start, fuel)
