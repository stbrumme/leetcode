class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        # union-find, copied from problem 721, simplified
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x]) # path compression
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        parent = list(range(n))

        # duplicate restrictions with swapped roles
        restrictions += [ ( b, a ) for a, b in restrictions ]
        prevent = [ set() for _ in range(n) ]
        for a, b in restrictions:
            prevent[a].add(b)

        for a, b in requests:
            one = find(a)
            two = find(b)

            # already friends
            if one == two:
                yield True
                continue

            # check restrictions (directly)
            if a in prevent[b]: # or b in prevent[a]:
                yield False
                continue

            # check restrictions (indirectly)
            allow = True
            for i, j in restrictions:
                if one == find(i) and two == find(j):
                    yield False
                    allow = False
                    break

            if allow:
                union(a, b)
                yield True
