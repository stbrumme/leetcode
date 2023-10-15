class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        if arrLen > 500:
            arrLen = 501

        dp = [ 0 ] * arrLen
        dp[0] = 1 # start at zero

        for s in range(steps):
            next = dp.copy()

            for i in range(arrLen):
                if i > 0:
                    next[i] += dp[i - 1]
                if i < arrLen - 1:
                    next[i] += dp[i + 1]

            dp = next

        return dp[0] % (10**9 + 7)
