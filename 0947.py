class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # all stones sharing a row or column create a subnet
        # => count all distinct subnets
        result = 0

        # union-find, copied from problem 721, simplified
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x]) # path compression
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        # identity
        parent = { x : x for x, y in stones }

        # group point into rows
        rows = {} # just store the first point
        for x, y in stones:
            if y in rows:
                union(rows[y], x)
            else:
                rows[y] = x

        # find distinct groups
        distinct = set([ find(rows[y]) for y in rows ])
        return len(stones) - len(distinct)
