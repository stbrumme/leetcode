class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        # count modulo k
        freq = [ 0 ] * k
        for a in arr:
            # find partner such that (mod + other) % k == 0
            mod   = a % k
            other = k - mod if mod > 0 else 0

            if  freq[other] > 0:
                freq[other] -= 1 # have a partner
            else:
                freq[mod]   += 1 # single for the win

        # all paired ?
        return sum(freq) == 0
