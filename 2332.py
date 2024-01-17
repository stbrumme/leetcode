class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        result = 0

        heapify(passengers)
        waiting = []    # passengers currently waiting for a bus (min-heap)
        boarded = set() # passengers riding any bus

        full = False
        for b in sorted(buses):
            # queue incoming passengers
            while passengers and passengers[0] <= b:
                heappush(waiting, heappop(passengers))

            # board as many as possible
            full = True
            for _ in range(capacity):
                if waiting:
                    boarded.add(heappop(waiting))
                else:
                    full = False
                    break

        # take last bus if it wasn't full
        if not full:
            if b not in boarded: # Python kept the variable b from the previous loop
                return b

        # replace the last person who boarded
        result = max(boarded) - 1
        while result in boarded:
            result -= 1
        return result
