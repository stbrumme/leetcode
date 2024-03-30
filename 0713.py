class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        result = 0
        if k <= 1: # impossible
            return 0

        left = 0
        have = 1
        for right in range(len(nums)):
            # extend array
            have *= nums[right]
            # shrink until product is strictly less than k
            while have >= k:
                have //= nums[left]
                left  += 1

            result += right - left + 1

        return result
