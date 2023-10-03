class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        total = sum(nums)

        # F(0)
        initial = 0
        for i, n in enumerate(nums):
            initial += i * n

        # F(n) = F(n-1) + sum(nums) - len(nums) * nums[n]
        best = current = initial
        for i in range(len(nums) - 1, 0, -1):
            current += total - len(nums) * nums[i]
            best = max(best, current)

        return best
