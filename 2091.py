class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        low = high = 0
        for i, n in enumerate(nums):
            if   n < nums[low]:
                low  = i
            elif n > nums[high]:
                high = i

        # three versions:
        # a) remove both from the left  side
        # b) remove both from the right side
        # c) remove one from the left, one from the right side
        a = max(low, high) + 1
        b = len(nums) - min(low, high)
        c = min(low, high) + 1 + (len(nums) - max(low, high))
        return min(a, b, c)
