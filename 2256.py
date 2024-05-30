class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        result = 0
        best   = +inf

        left  = 0
        right = sum(nums)
        size  = len(nums)
        for i, n in enumerate(nums, 1):
            # adjust sums
            left  += n
            right -= n

            avgLeft  = left  // i
            avgRight = 0 if size == i else right // (size - i)
            # not clearly defined edge case:
            # the right side can be empty, where the left side always has at least one element

            diff = abs(avgLeft - avgRight)
            if best > diff:
                best   = diff
                result = i - 1

        return result
