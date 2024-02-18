class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i]    *= 2
                nums[i + 1] = 0
        return sorted(nums, key = lambda x : 1 if x == 0 else 0) # Python has stable sort
