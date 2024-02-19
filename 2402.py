class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        rooms    = list(range(n)) # min-heap of available rooms
        ongoing  = []             # min-heap of active meetings ( end, room )
        occupied = [ 0 ] * n      # number of meetings held

        for s, e in sorted(meetings):
            # finished meeting
            while ongoing and ongoing[0][0] <= s:
                when, where = heappop(ongoing)
                heappush(rooms, where)

            # find room for upcoming meeting
            if rooms:
                # start on time
                where = heappop(rooms)
            else:
                # delayed meeting
                delayed, where = heappop(ongoing)
                e += delayed - s

            # start meeting
            heappush(ongoing, ( e, where ))
            occupied[where] += 1

        # find most popular room
        most = max(occupied)
        for i, o in enumerate(occupied):
            if o == most:
                return i
