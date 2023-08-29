class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        Nope = -9999999
        # 0 => ready, 1 => have stock, 2 => cooldown
        dp = [ 0, Nope, Nope ]
        for p in prices:
            next = [ 0, Nope, Nope ]

            next[0] = max(dp[0],     dp[2]) # was ready before or left cooldown
            next[1] = max(dp[0] - p, dp[1]) # buy or keep stock
            if dp[1] != Nope:               # sold stock, now cooldown
                next[2] = dp[1] + p

            dp = next

        return max(0, dp[0], dp[2])
