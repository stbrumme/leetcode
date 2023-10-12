class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        all = defaultdict(list)
        for x, y in points:
            all[x].append(y)
        for x in all:
            all[x].sort()

        allkeys = sorted(all.keys())
        # bisect along x and y axis to find the bounding box

        for x, y, r in queries:
            inside = 0

            minx = x - r
            maxx = x + r
            miny = y - r
            maxy = y + r
            r2 = r * r # avoid sqrt by using the square on both sides

            # fast test against bounding-box
            left  = bisect_left (allkeys, minx)
            right = bisect_right(allkeys, maxx)
            for i in range(left, right):
                xx = allkeys[i]

                scanline = all[xx]
                down = bisect_left (scanline, miny)
                up   = bisect_right(scanline, maxy)

                # exact test
                for j in range(down, up):
                    yy = scanline[j]
                    if (xx - x)**2 + (yy - y)**2 <= r2: # exact test
                        inside += 1

            yield inside
