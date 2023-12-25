class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)):
            result += sum(len(set(nums[i : j + 1])) ** 2 for j in range(i, len(nums)))
        return result
