class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        # create k - 1 distinct differences, followed by lots of 1s
        next = [ None, 1, n ]
        dir  = +1
        for i in range(n):
            yield next[dir]
            next[dir] +=  dir
            if i + 1 < k: # alternate direction
                dir    = -dir
