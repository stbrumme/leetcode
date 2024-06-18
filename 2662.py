class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        result = +inf
        sx, sy = start
        tx, ty = target

        size = len(specialRoads)
        best = [ +inf  ] * size
        seen = [ False ] * (size + 1)
        todo = [ ( 0, sx, sy, -1 ) ] # cost, exit x, exit y, index in specialRoads
        while todo:
            distance, x, y, id = heappop(todo)

            if seen[id]:
                continue
            seen[id] = True

            cost   = abs(x - tx) + abs(y - ty)
            result = min(result, distance + cost)

            for next, (ax, ay, bx, by, skip) in enumerate(specialRoads):
                if not seen[next]:
                    cost  = abs(x - ax) + abs(y - ay)
                    cost += distance + skip
                    if  best[next] > cost:
                        best[next] = cost
                        heappush(todo, ( cost, bx, by, next ))

        return result
