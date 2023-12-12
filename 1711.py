class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        items = defaultdict(int)
        for d in deliciousness:
            items[d] += 1

        high = max(items)

        result = 0
        for i in items:
            for exponent in range(21 + 1): # at most 2^20 per food
                two   = 1 << exponent
                other = two - i
                if other > high:
                    break
                if other <  i: # don't count twice, (a,b) is considered identical to (b,a)
                    continue
                if other == i:
                    result += (items[i] - 1) * items[i] // 2 # can't match an ingredient with itself
                elif other in items:
                    result += items[i] * items[other]

        return result % 1_000_000_007
