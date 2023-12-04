class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        # union-find, copied from problem 721
        parent = { i: i for i in range(len(s)) }

        def union(a, b):
            a = find(a)
            b = find(b)
            if a == b:
                return
            if a < b:
                parent[b] = a
            else:
                parent[a] = b

        def find(a):
            if parent[a] != a:
                parent[a] = find(parent[a]) # path compression
            return parent[a]

        # set up groups of connected positions
        for x, y in pairs:
            union(x, y)

        # collect letters for each group
        groups = defaultdict(list)
        for i, c in enumerate(s):
            groups[find(i)].append(c)
        # lowest first
        used = {}
        for g in groups:
            groups[g].sort()
            used[g] = 0

        result = ""
        for i in range(len(s)):
            # choose lowest letter for each group
            index = find(i)
            result      += groups[index][used[index]]
            used[index] += 1

        return result
