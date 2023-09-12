class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        right = left = best = zeros = 0
        while right < len(nums):
            if nums[right] == 0:
                zeros += 1
                while left < right and zeros > 1:
                    if nums[left] == 0:
                        zeros -= 1
                    left += 1

            right += 1
            best = max(best, right - left - 1)

        return best
