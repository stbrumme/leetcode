class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        stop2bus = defaultdict(set)
        for bus, stops in enumerate(routes):
            for s in stops:
                stop2bus[s].add(bus)

        if source not in stop2bus:
            return -1
        if target not in stop2bus:
            return -1

        todo  = { source: [] }
        seen  = set()
        changes = 1
        while todo:
            next = {}
            for stop in todo:
                seen.add(stop)
                busses = todo[stop]

                for b in stop2bus[stop]:
                    if b in busses:
                        continue

                    for r in routes[b]:
                        if r == target:
                            return changes
                        if r not in seen:
                            next[r] = busses + [ b ]

            changes += 1
            todo     = next

        return -1
