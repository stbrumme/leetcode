class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp = defaultdict(int) # positive index i: have stocks, it's the i-th transaction
                              # negative index i: no stocks, finished i transactions
        dp[0] = 0

        for p in prices:
            # do nothing
            next = dp.copy()

            for tx in sorted(dp.keys()):
                if tx >= k:
                    continue

                flip = -tx
                if tx >= 0:
                    # buy
                    if flip - 1 in dp:
                        next[flip - 1] = max(dp[flip - 1], dp[tx] - p)
                    else:
                        next[flip - 1] =                   dp[tx] - p
                else:
                    # sell
                    if flip in dp:
                        next[flip]     = max(next[flip],     dp[tx] + p)
                    else:
                        next[flip]     =                     dp[tx] + p

            dp = next

        return max(dp.values())
