class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        # the low score will always be zero (change to the same value as an existing element)
        # we only need to reduce the high score by removing the lowest and/or highest values
        nums.sort()
        a = nums[-3] - nums[0]
        b = nums[-2] - nums[1]
        c = nums[-1] - nums[2]
        return min(a, b, c)
