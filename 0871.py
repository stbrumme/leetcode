class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        result = 0

        stations.sort() # problem statement doesn't clarify whether stations are sorted by distance

        refuel   = []   # max-heap
        distance = startFuel
        while distance < target:
            # all reachable tank stops
            while stations and stations[0][0] <= distance:
                more = stations.pop(0)[1] # get more gas
                heappush(refuel, -more)   # max-heap => negative

            if not refuel:
                return -1 # out of gas

            # drive to the gas station with the largest refuel
            more      = -heappop(refuel) # negate again / max-heap
            distance += more             # extend the total range
            result   += 1

        return result
