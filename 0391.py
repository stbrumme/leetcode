class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        # extents
        minx = min([ r[0] for r in rectangles ])
        miny = min([ r[1] for r in rectangles ])
        maxx = max([ r[2] for r in rectangles ])
        maxy = max([ r[3] for r in rectangles ])

        # does area match ?
        need = (maxx - minx) * (maxy - miny)
        have = sum( (r[2] - r[0]) * (r[3] - r[1]) for r in rectangles)
        if need != have:
            return False

        # find out whether there is overlap and/or a gap
        points = defaultdict(int)
        for x, y, a, b in rectangles:
            points[( x, y )] += 1 # bottom-left
            points[( x, b )] += 1 # top-left
            points[( a, b )] += 1 # top-right
            points[( a, y )] += 1 # bottom-right

        # each point must be used 2 or 4 times, except the corners
        if points[( minx, miny )] != 1:
            return False
        if points[( maxx, miny )] != 1:
            return False
        if points[( maxx, maxy )] != 1:
            return False
        if points[( minx, maxy )] != 1:
            return False

        del points[( minx, miny )]
        del points[( maxx, miny )]
        del points[( maxx, maxy )]
        del points[( minx, maxy )]

        for p in points.values():
            if p != 2 and p != 4:
                return False

        return True
