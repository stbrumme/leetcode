class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = [ 0, -99999999 ] # 0 => wealth, own no stock, 1 => # wealth owning stock

        for p in prices:
            next = [ 0, 0 ]
            next[0] = max(dp[0], dp[1] + p)
            next[1] = max(dp[1], dp[0] - p - fee)
            dp = next

        return dp[0]
