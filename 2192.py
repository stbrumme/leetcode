class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        next = defaultdict(list)
        for a, b in edges:
            next[b].append(a) # reverse order

        @cache
        def deeper(node):
            result = set([ node ])
            for other in next[node]:
                result |= deeper(other)
            return result

        parent = [ set() for _ in range(n) ]
        for a, b in edges:
            parent[b] |= deeper(a)

        return [ sorted(p) for p in parent ]
