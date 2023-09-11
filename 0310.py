class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        connect = { }
        for i in range(n):
            connect[i] = set()

        for e in edges:
            connect[e[0]].add(e[1])
            connect[e[1]].add(e[0])

        # prune:
        # if there are multiple leafs for a node, then these leafs will never be the root
        prune = []
        for c in connect:
            current = connect[c]
            if len(current) == 1:
                (first,) = current
                if len(connect[first]) > 1:
                    prune.append(c)
        for p in prune:
            del connect[p]

        @cache
        def deeper(node, parent):
            # pruned ?
            if node not in connect:
                return 1

            longest = 0
            for c in connect[node]:
                if c != parent: # avoid loop
                    longest = max(longest, deeper(c, node))
            return longest + 1

        best = 99999999
        result = []
        for c in connect:
            current = deeper(c, c)
            if best > current:
                best = current
                result.clear()
            if best == current:
                result.append(c)

        return result
