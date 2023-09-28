class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        nums.sort()
        for i in range(len(nums)):
            if i > 0:
                if nums[i - 1] >= nums[i] - 1:
                    continue
            if i < len(nums) - 1:
                if nums[i + 1] <= nums[i] + 1:
                    continue

            yield nums[i]
