class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        next = defaultdict(list)
        for a, b, time in roads:
            next[a].append(( b, time ))
            next[b].append(( a, time ))

        todo = [ [ 0, 0, 1 ] ] # min-heap: time, intersection, ways
        seen = set()           # never visit a city twice because that can't be the shortest way
        while True:
            # shortest time
            now  = todo[0][0]
            same = defaultdict(int) # intersection, ways
            while todo and todo[0][0] == now:
                time, intersection, ways = heappop(todo)
                same[intersection] += ways
                seen.add(intersection)

            # process cities with same arrival time at once
            for s in same:
                ways = same[s] % 1_000_000_007
                if s == n - 1:
                    return ways

                for other, time in next[s]:
                    if other not in seen:
                        heappush(todo, ( now + time, other, ways ))
