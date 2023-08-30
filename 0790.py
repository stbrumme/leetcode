class Solution:
    def numTilings(self, n: int) -> int:
        zero   = defaultdict(int) # no tile used
        one    = defaultdict(int) # one tile in upper row
        two    = defaultdict(int) # two tiles in upper row
        bottom = defaultdict(int) # one tile in lower row

        zero[0] = 1

        for width in range(n+1):
            # domino up-down
            zero  [width] += zero  [width - 1]
            # domino left-right
            two   [width] += zero  [width - 2]
            zero  [width] += two   [width]
            one   [width] += bottom[width - 1]
            bottom[width] += one   [width - 1]
            # tromino down-right
            one   [width] += zero  [width - 2]
            # tromino up-right
            bottom[width] += zero  [width - 2]
            # tromino up-left
            zero  [width] += bottom[width - 1]
            # tromino down-left
            zero  [width] += one   [width - 1]

        return zero[n] % (10**9 + 7)
