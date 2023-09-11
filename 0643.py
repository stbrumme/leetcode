class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total  = sum(nums[:k-1])
        result = float("-inf")
        for i in range(k-1, len(nums)):
            total += nums[i]
            result = max(result, total / k)
            total -= nums[i - k + 1]

        return result
