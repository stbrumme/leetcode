class Solution:
    def minDifference(self, nums: List[int]) -> int:
        # very small dataset: make all equal
        if len(nums) <= 4:
            return 0

        nums.sort()

        result =             abs(nums[-4] - nums[0])  # modify the smallest three
        result = min(result, abs(nums[-3] - nums[1])) # smallest two plus the largest
        result = min(result, abs(nums[-2] - nums[2])) # smallest one plus the two largest
        result = min(result, abs(nums[-1] - nums[3])) # modify the largest three
        return result
