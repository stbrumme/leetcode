class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        height = len(nums)
        for i in range(height):
            nums[i].sort()

        result = 0
        while nums[0]:
            high = 0
            for i in range(height):
                high = max(high, nums[i].pop())
            result += high
        return result
