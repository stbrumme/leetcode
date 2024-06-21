class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        # strategy A:
        #   keep only root node
        # strategy B:
        #   set root to zero and apply strategy A or B to each child node
        # special case leaf node:
        #   score is always zero, because nullifying that single node isn't beautiful anymore

        size = len(values)

        # find neighbors
        next = [ list() for _ in range(size) ]
        for a, b in edges:
            next[a].append(b)
            next[b].append(a)

        # "fake" parent of root node, simplifies next[node].remove(parent)
        next[0].append(-1)

        # sum of current node and all subnodes
        # remove parent from next[], too
        high = [ -1 ] * size
        def limit(node, parent):
            next[node].remove(parent)

            high[node] = values[node]
            # sum of children
            for other in next[node]:
                high[node] += limit(other, node)
            return high[node]

        limit(0, -1)

        # high score for a node
        def deeper(node):
            # leaf
            if not next[node]:
                return 0

            # strategy A
            a = high[node]   - values[node]

            # strategy B
            b = values[node] + sum(deeper(other) for other in next[node])

            return max(a, b)

        return deeper(0)
