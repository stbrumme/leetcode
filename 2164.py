class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even = sorted(nums[ ::2])
        odd  = sorted(nums[1::2], reverse = True)
        for a, b in zip(even, odd):
            yield a
            yield b
        if len(nums) & 1:
            yield even[-1]
