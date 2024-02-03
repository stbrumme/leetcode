class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        maxbits = 24 # 2^24 > 10^7
        bits    = [ 0 ] * maxbits
        for n in candidates:
            mask = 1
            for i in range(maxbits):
                if n & mask: # count bit
                    bits[i] += 1

                if n < mask:     # for performance only
                    break

                mask *= 2

        return max(bits)
