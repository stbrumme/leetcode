class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        # add stop markers to simplify inner loop
        pos = [ -99999999 ] + [ i for i in range(len(s)) if s[i] == c ] + [ +99999999 ]

        scan = 1
        for i in range(len(s)):
            up   = abs(pos[scan    ] - i) # previous
            down = abs(pos[scan - 1] - i) # next
            if up == 0:
                scan += 1

            yield min(up, down)
