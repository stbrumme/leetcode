class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        # count changes
        delta = defaultdict(int)
        for a, b in ranges:
            delta[a] += 1
            delta[b] -= 1

        # distinct sections
        distinct = 0
        overlap  = 0 # number of interval currently overlapping
        for pos, change in sorted(delta.items()):
            overlap += change
            if overlap == 0:
                distinct += 1

        # ways = 2^distinct
        return pow(2, distinct, 1_000_000_007)
