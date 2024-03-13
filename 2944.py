class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        @cache
        def deeper(i):
            # pay current fruit
            pay = prices[i - 1]
            # maybe it's enough to get all remaining fruits
            if i + i >= len(prices):
                return pay

            # need to pay for more fruits, choose the cheapest sequence
            return pay + min(deeper(i + j + 1) for j in range(i + 1))

        return deeper(1)
