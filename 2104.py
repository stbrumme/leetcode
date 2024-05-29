class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        result = 0

        # prioritize memory-efficiency and code simplicity ...
        size = len(nums)
        for i in range(size):
            low = high = nums[i]
            for j in range(i, size):
                low  = min(low,  nums[j])
                high = max(high, nums[j])
                result += high - low

        return result
