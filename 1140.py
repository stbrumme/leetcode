class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        size   = len(piles)
        total  = sum(piles)
        remain = [] # stones left after reaching this position
        for p in piles:
            remain.append(total)
            total -= p

        @cache
        def deeper(pos,  m):
            # take all (but works without this, too)
            if pos + 2 * m >= size:
                return remain[pos]

            return remain[pos] - min(deeper(pos + take, max(m, take)) for take in range(1, 2 * m + 1))

        return deeper(0, 1)
