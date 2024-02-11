class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        low  = min(nums)
        high = max(nums)

        for n in nums:
            if low < n < high:
                return n

        return -1
