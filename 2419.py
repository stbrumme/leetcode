class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        result = 0

        # x AND y is maximized if x == y
        high = max(nums)

        have = 0
        for n in nums:
            if n == high:
                have  += 1
            else:
                result = max(result, have)
                have   = 0

        return max(result, have)
