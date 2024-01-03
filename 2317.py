class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        maxBit = 27 # log2(10**8) is about 26.5

        # count usage of all bits
        all    = [ 0 ] * maxBit
        for n in nums:
            for i in range(maxBit):
                if n & (1 << i):
                    all[i] += 1

        # we need odd counters for each bit position b to maximize the result
        # if there is an even counter then we can choose an x == 1 << b
        # and nums[i] where bit b is set such that that bit is cleared in the new nums[i]
        # in the end it's always possible to "fix" even counters
        # the maximum result is the set of all bits which were set in any nums[i]
        result = 0
        for i in range(maxBit):
            if all[i] > 0:
                result |= 1 << i

        return result
