class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()

        avgs  = set()
        left  = 0
        right = len(nums) - 1
        while left <= right:
            avgs.add(nums[left] + nums[right]) # no need to divide by 2
            left  += 1
            right -= 1

        return len(avgs)
