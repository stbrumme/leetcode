class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # let's avoid a full-blown sort
        # and do everything from scratch
        one = max(nums[0], nums[1]) # largest values
        two = min(nums[0], nums[1]) # second largest

        for i in range(2, len(nums)):
            x = nums[i]

            if one <= x:   # new largest value
                two, one = one, x
            elif two <  x: # not largest, but new second largest value
                two = x

        return (one - 1) * (two - 1)
