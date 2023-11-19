class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        # shortest short of a such that b fits
        aa = a
        result = 1
        while len(aa) < len(b):
            aa += a
            result += 1

        if b in aa:
            return result

        # maybe overlapping with borders
        aa     += a
        result += 1
        return result if b in aa else -1
