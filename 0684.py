class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # union-find, copied from problem 721
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x]) # path compression
            return parent[x]

        def union(x, y):
            x = find(x)
            y = find(y)
            if x == y:
                return
            if x < y:
                parent[y] = x
            else:
                parent[x] = y

        parent = [ i for i in range(len(edges) + 1) ] # one-based
        for a, b in edges:
            # if a and b are already connected, then the new edge is redundant
            if find(a) == find(b):
                return (a, b)

            union(a, b)
