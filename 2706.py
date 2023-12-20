class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        spend = prices[0] + prices[1]
        return money - spend if money >= spend else money
