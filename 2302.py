class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        result = 0

        size = len(nums)
        left = 0
        have = 0
        for right, n in enumerate(nums):
            # widen  sliding window
            have += n

            length = right - left + 1
            # shrink sliding window
            while have * length >= k:
                have   -= nums[left]
                left   += 1
                length -= 1

            result += length

        return result
