class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        size = len(nums)

        result = 0
        for left in range(size - 1):
            delta = nums[left + 1] - nums[left]
            for right in range(left + 1, size):
                if delta != nums[right] - nums[right - 1]:
                    break
                if right - left >= 2:
                    result += 1

        return result
