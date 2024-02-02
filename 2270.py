class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        result = 0
        left   = 0
        right  = sum(nums)
        for n in nums[:-1]:
            left  += n
            right -= n
            if left >= right:
                result += 1
        return result
