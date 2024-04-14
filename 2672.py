class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        have = [ 0 ] * (n + 2) # prepend and append an extra zero
        best = 0
        for pos, color in queries:
            pos += 1 # compensate for the prepended zero

            if have[pos - 1] == have[pos] and have[pos] != 0:
                best -= 1
            if have[pos + 1] == have[pos] and have[pos] != 0:
                best -= 1

            have[pos] = color

            if have[pos - 1] == have[pos]:
                best += 1 # same as before but add instead of subtract
            if have[pos + 1] == have[pos]:
                best += 1

            yield best
