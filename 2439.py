class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        result = 0

        # it's always possible to apply these operations such that
        # all values in a subarray have the same value or differ by at most 1
        total = 0
        for i, n in enumerate(nums, 1):
            total += n
            up     = (total + i - 1) // i # average, rounded up
            result = max(result, up)
        return result
