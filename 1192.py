class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # it took me quite a while to discover "Tarjan's algorithm" (never heard of it before)

        next = defaultdict(list)
        for a, b in connections:
            next[a].append(b)
            next[b].append(a)

        age = {} # timestamp when node was visited first
        low = {} # oldest reachable node
        now = 0  # timestamp

        def deeper(node, previous = None):
            nonlocal now, next, age, low

            # set timestamp
            age[node] = now
            low[node] = now
            now += 1

            for neighbor in next[node]:
                if neighbor == previous: # loop
                    continue

                # process neighbor (if not already done)
                if neighbor not in age:
                    yield from deeper(neighbor, node)

                # maybe found an older node
                low[node] = min(low[node], low[neighbor])

                if low[neighbor] > age[node]:
                    yield [ node, neighbor ]

        yield from deeper(0)
