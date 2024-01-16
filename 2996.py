class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # find prefix
        have = nums[0]
        i = 1
        while i < len(nums) and nums[i] == nums[i - 1] + 1:
            have += nums[i]
            i    += 1

        # look for missing integer
        while have in nums:
            have += 1

        return have
