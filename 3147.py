class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        have = [ 0 ] * k # = sum(energy[i % k])
        pos  = 0         # = i % k, avoid slow modulo
        for e in energy:
            # add to chain or restart a new chain
            have[pos] = max(have[pos] + e, e)

            pos += 1
            if pos == k:
                pos = 0

        return max(have)
