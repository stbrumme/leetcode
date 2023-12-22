class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        high  = 0
        total = 0
        for n in nums:
            high   = max(high, n)
            total += n + high
            yield total
