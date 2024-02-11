class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        result = +inf

        nums.sort()
        for a, b in zip(nums, nums[1:]):
            result = min(result, b - a)

        return result
