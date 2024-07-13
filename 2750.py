class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        # indexes of 1s
        ones = [ i for i, n in enumerate(nums) if n == 1 ]

        # no good at all
        if not ones:
            return 0

        result = 1
        for a, b in zip(ones, ones[1 :]):
            result *= b - a
            result %= 1_000_000_007

        return result
