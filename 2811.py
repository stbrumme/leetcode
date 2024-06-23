class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        # if there are two values a and b, that are located next to each other, and a + b >= m
        # then we can continuously chop off a single value on the left or right end of the array
        # and finally split a and b
        return len(nums) <= 2 or any(a + b >= m for a, b in zip(nums, nums[1 :]))
