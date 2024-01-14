class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        def value(row):
            result = 0
            for r in row:
                result <<= 1
                result  += r
            return result

        # count rows with the same or complement value
        have = defaultdict(int)
        for r in matrix:
            if r[0] == 0:
                have[value(r)] += 1
            else: # flip
                have[value([ 1 - rr for rr in r ])] += 1
        return max(have.values())
