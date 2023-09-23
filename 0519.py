class Solution:
    def two(self, i):
        return ( i % self.m, i // self.m )

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.limit = m * n
        self.reset()

    def flip(self) -> List[int]:
        if self.available:
            # lots of 1s
            result = self.available[-1]
            del self.available[-1]
        else:
            # more zeros than 1s
            result = self.two(randint(0, self.limit - 1))
            while result in self.avoid:
                result = self.two(randint(0, self.limit - 1))

        self.avoid.add(result)

        # same zeros as 1s
        if not self.available and len(self.avoid) * 2 >= self.limit:
            for i in range(self.limit):
                if self.two(i) not in self.avoid:
                    self.available.append(self.two(i))
            shuffle(self.available)

        return result

    def reset(self) -> None:
        self.avoid = set()
        self.available = []