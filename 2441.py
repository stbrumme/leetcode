class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort(reverse = True)

        right = len(nums) - 1
        for left, k in enumerate(nums):
            if k < 0:
                break

            # skip number with larger absolute value
            while k < -nums[right]:
                right -= 1
            if k == -nums[right]:
                return k

        return -1
