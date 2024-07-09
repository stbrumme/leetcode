class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        # highest node ID
        size = max(max(a, b) for a, b, weight in edges) + 1

        # build graph
        next = [ [] for _ in range(size) ]
        for a, b, weight in edges:
            next[a].append(( b, weight ))
            next[b].append(( a, weight ))

        # distance already modulo signalSpeed
        @cache
        def deeper(node, parent, distance):
            connectable = 1 if distance == 0 else 0

            # go deeper, avoid backtracking
            for other, weight in next[node]:
                if other != parent:
                    connectable += deeper(other, node, (distance + weight) % signalSpeed)

            return connectable

        # start from each node
        for node in range(size):
            # count connectable servers
            good = []
            for other, weight in next[node]:
                good.append(deeper(other, node, weight % signalSpeed))

            # all combinations
            total = sum(good)
            combinations = 0
            for g in good:
                total        -= g
                combinations += g * total

            yield combinations
