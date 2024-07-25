class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        result = 0

        size = len(nums)
        nums.sort()

        # compare large numbers in right half against small numbers in left half
        left = 0
        for right in range((size + 1) // 2, size):
            if nums[left] * 2 <= nums[right]:
                result += 2 # mark both
                left   += 1

        return result
