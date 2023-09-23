class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        pos  = 0
        have = [ i+1 for i in range(n) ]
        while len(have) > 1:
            pos += k-1
            pos %= len(have)
            del have[pos]
        return have[0]