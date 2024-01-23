class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        result = 0

        prev = 0
        have = 0
        for n in nums:
            if n > prev:
                have  += n
                result = max(result, have)
            else:
                have   = n

            prev = n

        return result
