class StockPrice:
    def __init__(self):
        self.ticks    = {}
        self.last     = 0
        self.lasttime = 0
        self.prices   = defaultdict(int)
        self.high     = 0
        self.low      = 2_000_000_000
        self.fixhigh  = False
        self.fixlow   = False

    def update(self, timestamp: int, price: int) -> None:
        if timestamp >= self.lasttime:
            self.last = price
            self.lasttime = timestamp

        # correcting a previous high or low
        if timestamp in self.ticks:
            previous = self.ticks[timestamp]
            self.fixlow  |= previous == self.low  and price > self.low
            self.fixhigh |= previous == self.high and price < self.high
            self.prices[previous] -= 1
            if self.prices[previous] == 0:
                del self.prices[previous]

        self.prices[price] += 1

        self.ticks[timestamp] = price
        self.low  = min(self.low,  price)
        self.high = max(self.high, price)

    def current(self) -> int:
        return self.last

    def maximum(self) -> int:
        if self.fixhigh: # find new high
            self.high    = max(self.prices)
            self.fixhigh = False
        return self.high

    def minimum(self) -> int:
        if self.fixlow: # find new high/low
            self.low    = min(self.prices)
            self.fixlow = False
        return self.low
