class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        # union-find, copied from problem 721, simplified
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x]) # path compression
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        parent = [ i for i in range(n) ]

        # run union-find
        for a, b in edges:
            union(a, b)

        # find distinct groups
        groups = defaultdict(int)
        for i in range(n):
            groups[find(i)] += 1

        return sum(g * (n - g) for g in groups.values()) // 2 # each pair was counted twice
