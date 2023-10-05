class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = {}
        for c in s1 + s2 + baseStr:
            parent[c] = c

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

        # mapping such that parent is minimized
        for a, b in zip(s1, s2):
            union(a, b)

        # and resolve
        return "".join([ find(c) for c in baseStr ])
