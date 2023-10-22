class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        result = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                result += nums[i] + nums[j] < target
        return result
