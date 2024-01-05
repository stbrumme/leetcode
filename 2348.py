class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        result = 0

        zeros = 0
        for n in nums: # padding
            if n == 0:
                zeros  += 1
                result += zeros
            else:
                zeros   = 0

        return result
