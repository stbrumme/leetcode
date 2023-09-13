class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        size = len(isConnected)

        # union find algo
        parent = [ i for i in range(size) ]

        def union(x, y):
            parent[find(max(x, y))] = find(min(x, y))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        for i in range(size):
            for j in range(i + 1, size):
                if isConnected[i][j] == 1:
                    union(i, j)

        # distinct parents
        distinct = set([ find(i) for i in range(size) ])
        return len(distinct)
