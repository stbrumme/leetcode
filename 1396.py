class UndergroundSystem:
    def __init__(self):
        self.total   = defaultdict(int)
        self.rides   = defaultdict(int)
        self.ongoing = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.ongoing[id] = ( stationName, t )

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startT = self.ongoing[id]
        # not needed, but always good to clean up
        del self.ongoing[id]

        key = ( startStation, stationName )
        self.total[key] += t - startT
        self.rides[key] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = ( startStation, endStation )
        return self.total[key] / self.rides[key]
