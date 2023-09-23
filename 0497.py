class Solution:
    def __init__(self, rects: List[List[int]]):
        self.rects  = rects
        self.points = {}
        self.total  = 0
        for i,r in enumerate(rects):
            area = (r[2] - r[0] + 1) * (r[3] - r[1] + 1) # not actual area, tough lesson ...
            self.total += area
            self.points[self.total] = i

    def pick(self) -> List[int]:
        i = randint(0, self.total - 1)
        # TODO: use binary search
        r = None
        for p in sorted(self.points):
            if p > i:
                r = self.rects[self.points[p]]
                return [ randint(r[0], r[2]), randint(r[1], r[3]) ]