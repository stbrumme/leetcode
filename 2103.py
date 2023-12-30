class Solution:
    def countPoints(self, rings: str) -> int:
        have = [ 0 ] * 10
        for i in range(0, len(rings), 2):
            color =     rings[i]
            rod   = int(rings[i + 1])
            if   color == "R":
                have[rod] |= 1
            elif color == "G":
                have[rod] |= 2
            elif color == "B":
                have[rod] |= 4
        return sum(1 for h in have if h == 1+2+4)
