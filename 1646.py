class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        # https://oeis.org/A002487
        if n <= 1:
            return n
        nums = [ 0 ] * (n + 1)
        nums[1] = 1
        for i in range(2, n + 1):
            half = i >> 1
            if i & 1:
                nums[i] = nums[half] + nums[half + 1]
            else:
                nums[i] = nums[half]
        return max(nums)
