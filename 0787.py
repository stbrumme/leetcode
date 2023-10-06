class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # from => to = price
        all = defaultdict(dict)
        for f in flights:
            all[f[0]][f[1]] = f[2]

        seen = {}                  # only visit a city again if we need less stops to get there

        schedule = [ (0, 0, src) ] # heap (total price, stops, city)
        while schedule:
            total, stops, city = heappop(schedule)

            # yeah ...
            if city == dst:
                return total

            seen[city] = stops

            # continue flight
            for next in all[city]:
                if stops <= k and (next not in seen or seen[next] > stops):
                    price = all[city][next]
                    heappush(schedule, (total + price, stops + 1, next))

        return -1
