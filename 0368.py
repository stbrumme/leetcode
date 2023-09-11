class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        dp = { } # highest number of the set => set's length
        dp[1] = 0
        longest = 0
        high    = 1

        for n in sorted(nums):
            add = defaultdict(int)
            for d in dp:
                if n % d == 0 and add[n] < dp[d] + 1:
                    add[n] = dp[d] + 1
                    if longest < add[n]:
                        longest = add[n]
                        high    = n

            for a in add:
                dp[a] = add[a]

        reverse = defaultdict(set)
        for d in dp:
            reverse[dp[d]].add(d)

        result = []
        for i in range(longest, 0, -1):
            for r in reverse[i]:
                if high % r == 0:
                    result += [ r ]
                    high = r
                    break

        return result
