class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        result = 1

        need = nums[0] + nums[1]
        for i in range(2, len(nums) - 1, 2):
            have = nums[i] + nums[i + 1]
            if have != need:
                break
            result += 1

        return result
