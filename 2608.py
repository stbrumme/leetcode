class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        result = +inf

        # build graph
        vertices = defaultdict(list)
        for u, v in edges:
            vertices[u].append(v)
            vertices[v].append(u)

        for start in range(n):
            # breadth-first search
            steps = 0
            seen  = { start: 0 }
            todo  = set([ start ])
            while todo and steps < result:
                next = set()

                for t in todo:
                    for v in vertices[t]:
                        if v in seen:
                            if seen[v] >= seen[t]: # seen both nodes before
                                # there are three known nodes
                                # start, t und v
                                # we know the distance from start to t
                                # we know the distance from start to v
                                # t and u share an edge
                                # cycle = length(start to t) + length(start to v) + length(t to v)
                                #       = length(start to t) + length(start to v) + 1
                                result = min(result, seen[v] + seen[t] + 1)
                        else:
                            # new
                            seen[v] = steps + 1
                            next.add(v)

                todo   = next
                steps += 1

        return result if result != +inf else -1
