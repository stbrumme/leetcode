class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        # rectangles: sorted widths
        top  = [ [] for _ in range(100 + 1) ]
        for x, y in rectangles:
            top[y].append(x)
        for t in top:
            t.sort()

        # remove unused lists
        while not top[-1]:
            top.pop()

        for x, y in points:
            yield sum(len(t) - bisect_left(t, x) for t in top[y :])
