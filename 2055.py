class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        prefix = [ 0 ] * len(s)
        # precomputation: count stars before each candle "prefix sum"
        stars    = 0
        complete = 0
        for i, c in enumerate(s):
            if c == "*":
                stars += 1
            else:
                complete = stars

            prefix[i] = complete

        # process queries
        for a, b in queries:
            # find left-most candle
            first = s.find("|", a, b + 1)

            # no candles in that range
            if first == -1:
                yield 0
                continue

            # find right-most candle
            last = s.rfind("|", a, b + 1)

            yield prefix[last] - prefix[first]
