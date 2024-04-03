class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        result = 0

        freq = defaultdict(int) # count per value
        same = defaultdict(set) # values with the same count

        for i, n in enumerate(nums):
            old = freq[n]
            new = old + 1

            # update counters
            freq[n] = old + 1
            if old > 0:
                same[old].discard(n)
                if not same[old]: # remove unused
                    del same[old]
            same[new].add(n)

            length = i + 1 # zero-index to one-indexed

            # it took quite a few attempts to correctly address all cases ...
            if len(freq) == 1:
                result = length # always the same number
            if len(same) <= 2 and 1 in same and len(same[1]) == 1:
                result = length # all same length except a single outlier
            if len(same) == 2 and len(same[max(same)]) == 1 and max(same) == 1 + min(same):
                result = length # frequency differs by one
            if max(same) == 1:
                result = length # each number at most once

        return result
