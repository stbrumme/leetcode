class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def distance(a, b): # no need for sqrt if only comparing for equality
            x1, y1 = a
            x2, y2 = b
            return (x1 - x2)**2 + (y1 - y2)**2

        # centre
        x = (p1[0] + p2[0] + p3[0] + p4[0]) / 4
        y = (p1[1] + p2[1] + p3[1] + p4[1]) / 4
        c = (x, y)

        # all points must have same distance to the centre
        d1 = distance(p1, c)
        d2 = distance(p1, c)
        d3 = distance(p1, c)
        d4 = distance(p1, c)
        if not (d1 == d2 and d2 == d3 and d3 == d4):
            return False

        # now make sure all sides have the same length
        sides = set()
        sides.add(distance(p1, p2))
        sides.add(distance(p1, p3))
        sides.add(distance(p1, p4))
        sides.add(distance(p2, p3))
        sides.add(distance(p2, p4))
        sides.add(distance(p3, p4))
        # some lines go through the centre, the others are true sides of the square
        return len(sides) == 2 and 0 not in sides # no degenerated squares
