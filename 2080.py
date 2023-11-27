class RangeFreqQuery:
    def __init__(self, arr: List[int]):
        self.pos = defaultdict(list)
        for i, a in enumerate(arr):
            self.pos[a].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        l = bisect_left (self.pos[value], left)
        r = bisect_right(self.pos[value], right)
        return r - l
