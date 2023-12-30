class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left  = 0
        right = sum(nums)
        for n in nums:
            right -= n
            yield abs(left - right)
            left  += n
