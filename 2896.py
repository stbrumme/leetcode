class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        # an even number of ones in both strings
        total = lambda a, b: int(a) + int(b)
        if (int(reduce(total, s1)) + int(reduce(total, s2))) % 2 == 1:
            return -1

        # mismatched positions
        mismatch = [ i for i in range(len(s1)) if s1[i] != s2[i] ]

        # apply one of both methods can lead to two outcomes:
        # a) fix two mismatches
        # b) fix one mismatch and create a new one

        # method 1: i and j can be chosen such that it always fixes two mismatches
        # method 2: keep swapping consecutive positions until hitting a second mismatch
        #           => total cost is the distance between those two mismatches

        @cache
        def deeper(i):
            if i >= len(mismatch):
                return 0

            # method 1: swap s1[i] and s1[j]
            best = deeper(i + 1) + x / 2 # correct one of two mismatches, each "costs" half of x
            # method 2: swap s1[i] and s1[i + 1]
            if i < len(mismatch) - 1:
                # consecutive swaps
                gap  = mismatch[i + 1] - mismatch[i]
                best = min(best, deeper(i + 2) + gap) # by skipping deeper(i + 1) we fixed 2 mismatches

            return best

        return round(deeper(0)) # deeper() returns a float but Leetcode requires int
                                # (fraction is always zero anyway)
