class Solution:
    def numOfWays(self, n: int) -> int:
        modulo = 1_000_000_007

        match = {}
        for a in range(3):
            for b in range(3):
                for c in range(3):
                    if a != b and b != c:
                        match[str(a) + str(b) + str(c)] = []
                        # 010, 012, 020, 021, 101, 102, 120, 121, 201, 202, 210, 212

        # figure out for each valid row what rows are "compatible" (can be painted next to it)
        for x in match:
            for y in match:
                if x[0] != y[0] and x[1] != y[1] and x[2] != y[2]:
                    match[x].append(y)

        have = { row : 1 for row in match } # 12 ones

        for i in range(n - 1):
            next = { row : 0 for row in match }
            for pattern in have:
                for follow in match[pattern]:
                    next[follow] += have[pattern]
            have = next

        return sum(have.values()) % modulo
