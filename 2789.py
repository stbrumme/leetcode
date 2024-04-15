class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        result = max(nums)

        increasing = -inf
        for n in reversed(nums):
            if n <= increasing:
                increasing += n
                result = max(result, increasing)
            else:
                increasing  = n

        return result
