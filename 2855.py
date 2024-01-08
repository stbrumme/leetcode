class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        # locate smallest number
        low = min(nums)
        pos = nums.index(low)

        # shift and check if sorted
        shifted = nums[pos:] + nums[:pos]
        if shifted != sorted(shifted):
            return -1

        return 0 if pos == 0 else len(nums) - pos
