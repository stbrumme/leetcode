class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        result = 0

        size = len(nums)
        high = max(nums)

        left = 0
        have = 0
        # sliding window which contains the maximum element less than k times
        for right in range(size):
            # extend on the right side
            if nums[right] == high:
                have += 1

            # shrink on the left side
            while have == k:
                if nums[left] == high:
                    have -= 1
                left += 1

            # all subarrays on the left side of the sliding window are okay
            result += left

        return result
