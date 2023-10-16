class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        size = len(strs)
        parent = [ i for i in range(size) ]
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

        # group all words with at most two different letters
        for i in range(size):
            for j in range(i + 1, size):
                a = strs[i]
                b = strs[j]

                # count diffs
                count = 0
                for k in range(len(a)):
                    if a[k] != b[k]:
                        count += 1

                # similar
                if count <= 2:
                    union(i, j)

        # count distinct parents
        groups = set()
        for i in range(len(parent)):
            groups.add(find(i))
        return len(groups)
