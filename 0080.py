class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return None

        if len(nums) <= 2:
            return len(nums)

        # pass 1: mark duplicates
        REMOVE = 99999999
        for i in range(2, len(nums)):
            if nums[i] == nums[i - 1] and nums[i] == nums[i - 2]:
                nums[i - 2] = REMOVE

        # pass 2: remove them
        skip = 0
        i = 0
        while i < len(nums):
            while nums[i] == REMOVE:
                i    += 1
                skip += 1
            nums[i - skip] = nums[i]
            i += 1

        return len(nums) - skip
