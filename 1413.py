class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        low  = 0
        have = 0
        for n in nums:
            have += n
            low   = min(low, have)

        return 1 - low
