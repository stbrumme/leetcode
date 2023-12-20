class Solution:
    def check(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                unrotated = nums[i:] + nums[:i]
                return unrotated == sorted(unrotated)

        return True
