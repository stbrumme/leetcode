class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        t = sorted([ i for i in s ], reverse = True)
        return "".join(t[1:] + t[:1]) # move a "1" to the end
