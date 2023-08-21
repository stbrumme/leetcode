class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        for i in range(1, len(prices)):
            change = prices[i] - prices[i-1]
            if change > 0:
                total += change
        return total
