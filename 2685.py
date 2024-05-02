class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        result = 0

        # union-find, copied from problem 721, simplified
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x]) # path compression
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        parent = list(range(n))

        # ensure edges are unique
        unique = set()
        for a, b in edges:
            unique.add(( min(a, b), max(a, b) ))

        # union nodes
        for a, b in unique:
            union(a, b)

        # find partitions
        parts = defaultdict(list)
        for i in range(n):
            parts[find(i)].append(i)

        for nodes in parts.values():
            # each node must be connected to each other node in current partition
            connected = 1
            for i, a in enumerate(nodes):
                if connected == 1:
                    for b in nodes[i + 1:]:
                        if ( a, b ) not in unique:
                            connected = 0
                            break

            result += connected

        return result
