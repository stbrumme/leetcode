class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # visit all roads
        # we are looking for the reachable road with the lowest distance
        result = +inf

        edges = defaultdict(list)
        for a, b, cost in roads:
            edges[a].append((cost, b))
            edges[b].append((cost, a))

        todo = [ 1 ] # start from city 1
        seen = [ False ] * (n + 1)
        while todo:
            city = todo.pop()
            # avoid loops
            if seen[city]:
                continue
            seen[city] = True

            for score, next in edges[city]:
                result = min(result, score)
                todo.append(next)

        return result
