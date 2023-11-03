class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        size  = len(nums)
        right = sum(nums)
        left  = 0
        prev  = 0
        for i, n in enumerate(nums):
            delta  = n - prev
            left  += delta * i
            right -= delta * (size - i)
            yield left + right
            prev = n
