class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        result = 0

        # 1,000,000th problem based on Kadane's algorithm
        high = low = 0
        for n in nums:
            high   = max(n, high + n)
            low    = min(n, low  + n)
            result = max(result, abs(high), abs(low))

        return result
