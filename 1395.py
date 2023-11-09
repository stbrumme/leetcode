class Solution:
    def numTeams(self, rating: List[int]) -> int:
        result = 0

        seen = set()            # i of one soldier
        up   = defaultdict(int) # j for two soldiers where r[i] < r[j]
        down = defaultdict(int) # j for two soldiers where r[i] > r[j]

        for r in rating:
            # triples
            for u in up:
                if r > u:
                    result += up[u]
            for d in down:
                if r < d:
                    result += down[d]

            # pairs
            for s in seen:
                if s < r:
                    up[r]   += 1
                else:
                    down[r] += 1

            seen.add(r)

        return result
