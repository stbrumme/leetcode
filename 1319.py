class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        # union-find, copied from problem 721, simplified
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x]) # path compression
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        parent = list(range(n))

        spare = 0 # redundant cables
        for a, b in connections:
            # already connected, can steal that cable
            if find(a) == find(b):
                spare += 1
            else:
                union(a, b)

        # number of disconnected networks
        disjunct = len(set([ find(i) for i in range(n) ]))
        # need one less cable to reconnect all of them
        need = disjunct - 1
        if spare >= need:
            return need
        else:
            return -1
