class Solution:
    def minOperations(self, nums: List[int]) -> int:
        result = 0

        flip = 0
        for n in nums:
            if n == flip:
                flip   ^= 1
                result += 1

        return result
