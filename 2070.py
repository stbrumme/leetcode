class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        # sort by price (ascending), then beauty (descending)
        pareto = [] # items where no other is cheaper and more beautiful
        for price, beauty in sorted(items, key = lambda x : x[0] * 10**10 - x[1]):
            if not pareto or beauty > pareto[-1][1]:
                pareto.append(( price, beauty ))

        for q in queries:
            # binary search
            pos = bisect_right(pareto, ( q + 1, 0 )) - 1
            if pos >= 0:
                yield pareto[pos][1]
            else:
                yield 0
