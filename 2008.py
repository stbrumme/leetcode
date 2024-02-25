class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        # collect start positions of all rides
        pickup = defaultdict(list)
        for s, e, t in rides:
            pickup[s].append(( t, e ))

        @cache
        def deeper(pos = 0):
            if pos >= n:
                return 0

            # drive without a passenger to next pickup position
            next = pos + 1
            while next < n and next not in pickup:
                next += 1
            best = deeper(next)

            # or pick up a passenger at current position
            for t, e in pickup[pos]:
                earn = e - pos + t
                best = max(best, earn + deeper(e))

            return best

        return deeper()
