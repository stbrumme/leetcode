class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        size = len(stations)

        # range-limited prefix/suffix sum, the lazy way ...
        @cache
        def left(pos, all = False):
            if pos <= 0 or r == 0:
                return 0

            result = stations[pos - 1] + left(pos - 1, True)
            return result if all else result - left(pos - r, True)

        @cache
        def right(pos, all = False):
            if pos >= size - 1 or r == 0:
                return 0

            result = stations[pos + 1] + right(pos + 1, True)
            return result if all else result - right(pos + r, True)

        # current power
        score = [ left(i) + stations[i] + right(i) for i in range(size) ]

        # True if there's no way to reach that power level for each city
        def impossible(power):
            build = [ 0 ] * size # additional power plants
            have  = 0            # = sum(build[i - r ... i + r])

            available = k
            for i, s in enumerate(score):
                # remove power plants too far on the left side
                left  = i - r
                right = i + r
                if left > 0:
                    have -= build[left - 1]

                # build new power plants
                need = power - (s + have)
                if need > 0:
                    have      += need
                    available -= need
                    if available < 0:
                        return True         # need more power plants than we are allowed to build
                    if right < size:
                        build[right] = need # build as far as possible on the right side

            return False

        limit = max(stations) * (2 * r + 1) + k
        return bisect_left(range(limit + 1), True, key = impossible) - 1
