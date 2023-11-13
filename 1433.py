class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        x = sorted([ c for c in s1 ])
        y = sorted([ c for c in s2 ])
        return all( a >= b for a, b in zip(x, y) ) or \
               all( a <= b for a, b in zip(x, y) )
