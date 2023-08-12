class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # the old XOR trick ...
        xor = 0
        for i in nums:
            xor = xor ^ i

        for i in range(1, len(nums)+1):
            xor = xor ^ i

        return xor
