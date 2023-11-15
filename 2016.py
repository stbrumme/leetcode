class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        result = -1
        low = high = nums[0]
        for n in nums:
            if low > n:
                low = high = n
            if high < n:
                high = n
                result = max(result, high - low)

        return result
