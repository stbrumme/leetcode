class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        left  = 0
        right = sum(nums)
        for i, n in enumerate(nums):
            right -= n
            if left == right:
                return i
            left  += n
        return -1
