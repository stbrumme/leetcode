class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        result = 0
        modulo = 1_000_000_007

        have = [ defaultdict(int) for _ in range(n + 1) ]
        have[0][0] = 1 # seed value: no crimes committed yet

        crimes = [ ( g, p ) for g, p in zip(group, profit) ]
        for gangsters, gain in sorted(crimes):
            for worked in reversed(range(n + 1)): # order is important to avoid self-references
                for money, schemes in have[worked].items():
                    # commit only crimes if there are enough gangsters
                    if worked + gangsters <= n:
                        total = money + gain
                        total = min(total, minProfit) # less entries
                        have[worked + gangsters][total] += schemes

        for h in have:
            for money, schemes in h.items():
                if money >= minProfit:
                    result += schemes

        return result % modulo
