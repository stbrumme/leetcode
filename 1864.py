class Solution:
    def minSwaps(self, s: str) -> int:
        result = +inf

        # count misplaced "0" and "1"
        diff0 = [ 0, 0 ] # start with "0"
        diff1 = [ 0, 0 ] # start with "1"
        for i, c in enumerate(s):
            c = ord(c) & 1
            if c == (i & 1):
                diff1[c] += 1
            else:
                diff0[c] += 1

        # number of misplaced bits must be the same
        # try to minimize it
        if diff0[0] == diff0[1]:
            result = min(result, diff0[0])
        if diff1[0] == diff1[1]:
            result = min(result, diff1[0])

        return result if result != +inf else -1
