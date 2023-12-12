class DetectSquares:
    def __init__(self):
        self.x  = defaultdict(list)
        self.y  = defaultdict(list)
        self.xy = []

    def add(self, point: List[int]) -> None:
        x, y = point
        self.x[x].append(y)
        self.y[y].append(x)
        self.xy.append(point)

    def count(self, point: List[int]) -> int:
        result = 0
        x, y = point
        col  = self.x[x]
        row  = self.y[y]
        for a, b in self.xy:
            # look for non-empty squares
            dx = abs(a - x)
            dy = abs(b - y)
            if dx == dy and dx > 0:
                # still need the other two points
                if b in col and a in row:
                    result += col.count(b) * row.count(a)
        return result
