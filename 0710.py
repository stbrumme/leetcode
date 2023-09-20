class Solution:
    def __init__(self, n: int, blacklist: List[int]):
        self.limit = n - 1 - len(blacklist)
        self.change = {}

        outside = self.limit
        avoid   = set(blacklist)
        shuffle(blacklist)
        for b in blacklist:
            if b <= self.limit:
                outside += 1
                while outside in avoid:
                    outside += 1
                self.change[b] = outside

    def pick(self) -> int:
        r = randint(0, self.limit)
        return self.change[r] if r in self.change else r
