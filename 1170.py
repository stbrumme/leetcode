class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        # f() according to problem
        f = lambda w : w.count(min(w))

        # precompute f(words)
        freq = defaultdict(int)
        for w in words:
            freq[f(w)] += 1

        cumulative = { 0 : len(words), 99999 : 0 } # edge cases
        # cumulative version of freq
        total = len(words)
        for x in sorted(freq):
            total -= freq[x]
            cumulative[x] = total

        # faster lookup via binary search
        thresholds = list(sorted(cumulative.keys()))

        # and finally start processing the queries
        for q in queries:
            value = f(q)
            pos = bisect_right(thresholds, value) - 1
            key = thresholds[pos]
            yield cumulative[key]
