class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        middle = nums[len(nums) // 2] # median
        return sum(abs(n - middle) for n in nums)
