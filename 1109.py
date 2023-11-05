class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        # min-heap based on "first"
        departure = []
        for b in bookings:
            departure.append(( b ))
        heapify(departure)

        # min-heap based on "last"
        active = []

        seats  = 0
        for i in range(1, n + 1):
            # starting on current day
            while departure and departure[0][0] == i:
                add = heappop(departure)
                heappush(active, ( add[1], add[2] ))
                seats += add[2]

            yield seats

            # arriving on current day
            while active and active[0][0] == i:
                remove = heappop(active)
                seats -= remove[1]
