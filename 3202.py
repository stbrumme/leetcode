class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        # longest sequence with modulo k
        # and the last two numbers being a and b
        # but there's no need to store a and b, it's sufficient to store a % k and b % k

        # sequences become [ a % k, b % k, a % k, b % k, ... ]

        for i in range(len(nums)):
            nums[i] %= k

        candidates = set(nums)

        longest = { n : [ 0 ] * k for n in nums } # replacing [ 0 ] * k by a dict() makes it slower
        for n in nums:
            for previous in candidates:
                longest[n][previous] = longest[previous][n] + 1

        return max(max(l) for l in longest.values())
