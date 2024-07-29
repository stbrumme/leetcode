class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        result = 0
        size = len(nums)

        # prefix sum (in-place)
        total = 0
        for i in range(size):
            total  += nums[i]
            nums[i] = total

        for i, left in enumerate(nums):
            # mid >= left, but the prefix includes left, too, therefore 2*left
            lowMid  = left + left
            # split even between mid and right
            highMid = (total + left) // 2

            low     = bisect_left (nums, lowMid,  lo = i + 1) # lo avoids edge cases with nums[i] = 0
            high    = bisect_right(nums, highMid, lo = low, hi = size - 1)
            result += high - low

        return result % 1_000_000_007
