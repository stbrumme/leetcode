class SeatManager:
    def __init__(self, n: int):
        # min-heap
        self.free = list(range(1, n + 1))

    def reserve(self) -> int:
        return heappop(self.free)

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.free, seatNumber)
