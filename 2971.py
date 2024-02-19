class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        total = sum(nums)
        # remove longest side if longer than the remaining sides
        while nums and nums[-1] >= total - nums[-1]:
            total -= nums.pop()

        return total if len(nums) >= 3 else -1 # at least three sides left
