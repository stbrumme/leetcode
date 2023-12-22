class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        freq = defaultdict(int)
        for c in costs:
            freq[c] += 1

        result = 0
        # least expensive first
        for f in sorted(freq):
            if f > coins:
                break
            # greedy: take as much as possible / available
            take    = min(coins // f, freq[f])
            coins  -= take * f
            result += take
        return result
