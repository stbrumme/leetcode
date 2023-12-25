class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        result = 0
        for i in range(len(nums)):
            result += sum(1 for j in range(i + 1, len(nums)) if abs(nums[i] - nums[j]) == k)
        return result
