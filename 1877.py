class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        result = 0
        nums.sort()
        for left in range(len(nums) // 2):
            # pair small with large numbers
            right = len(nums) - left - 1
            s = nums[left] + nums[right]
            result = max(result, s)
        return result
