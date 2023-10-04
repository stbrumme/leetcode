class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        result  = 1
        current = 1

        seed = nums[0]
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                current += 1
            else:
                result  = max(result, current)
                current = 1
                seed = nums[i]
        return max(result, current) # don't forget about the last subsequence ...
