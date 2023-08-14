class Solution:
    def countElements(self, nums: List[int]) -> int:
        high = max(nums)
        low  = min(nums)
        result = 0
        for i in nums:
            if i != high and i != low:
                result += 1

        return result
