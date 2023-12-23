class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        have = 0
        for n in nums:
            have += n
            yield have
