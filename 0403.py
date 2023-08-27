class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if 1 not in stones:
            return False

        del stones[0] # == 0

        dp = {}
        for s in stones:
            dp[s] = set()
        dp[1] = set([ 1 ])

        for s in stones:
            for k in dp[s]:
                if k > 1 and s + k - 1 in dp:
                    dp[s + k - 1].add(k - 1)
                if k > 0 and s + k     in dp:
                    dp[s + k].    add(k)
                if           s + k + 1 in dp:
                    dp[s + k + 1].add(k + 1)

        last = max(stones)
        return len(dp[last]) > 0
