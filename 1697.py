class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # idea: incremental union-find, connect short edges first and evaluate related queries

        # union-find, copied from problem 721, simplified
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x]) # path compression
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        parent = list(range(n))

        edges = [] # min-heap, shortest edges first
        for u, v, weight in edgeList:
            heappush(edges, ( weight, u, v ))

        size   = len(queries)
        result = [ 0 ] * size
        for i in sorted(range(size), key = lambda x : queries[x][2]): # queries with low limit come first
            p, q, limit = queries[i]

            # add all edges up to the current limit
            while edges and edges[0][0] < limit:
                weight, u, v = heappop(edges)
                union(u, v)

            # same (sub)net ?
            result[i] = find(p) == find(q)

        return result
