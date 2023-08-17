class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        sums = []
        total = 0
        for n in nums:
            total = max(total, 0) + n
            sums.append(total)

        return max(sums)
