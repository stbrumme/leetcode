class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        result = 0

        nums.sort()
        pos    = len(nums) // 2
        median = nums[pos]

        if median >  k:
            while pos >= 0 and nums[pos] > k:
                result += nums[pos] - k
                pos -= 1
        else:
            while pos < len(nums) and nums[pos] < k:
                result += k - nums[pos]
                pos += 1

        return result
