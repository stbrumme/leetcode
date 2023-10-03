class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        for n in nums:
            yield nums[n]
