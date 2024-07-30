class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        total = sum(nums)
        one   = sum(n for n in nums if       n <  10)
        two   = sum(n for n in nums if 10 <= n < 100)
        return one > total - one or two > total - two
