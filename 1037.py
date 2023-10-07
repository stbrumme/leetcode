class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        # more readable variables
        x1, y1 = points[0]
        x2, y2 = points[1]
        x3, y3 = points[2]

        # must be distinct
        if x1 == x2 and y1 == y2:
            return False
        if x1 == x3 and y1 == y3:
            return False
        if x2 == x3 and y2 == y3:
            return False

        # point1 becomes the origin
        x2 -= x1
        y2 -= y1
        x3 -= x1
        y3 -= y1

        # degenerated cases
        if x2 == 0 and x3 == 0:
            return False
        if y2 == 0 and y3 == 0:
            return False

        # angles with x axis
        a2 = y2 / (x2 + 10**-10) # avoid div-by-zero
        a3 = y3 / (x3 + 10**-10) # avoid div-by-zero

        # fix rounding issues
        def same(i, j):
            epsilon = 10**-5
            return abs(i - j) < epsilon

        return not same(a2, a3)
