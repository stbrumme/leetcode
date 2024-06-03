class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        result = -1

        size = len(edges)
        seen = set([ -1 ])
        for node in range(size):
            # already done
            if node in seen:
                continue
            # no outgoing edge
            if edges[node] == -1:
                continue

            # follow edges
            step = 0
            path = {}
            next = node
            while next not in seen: # until encountering either -1 or a known node
                seen.add(next)
                path[next] = step
                step += 1
                next  = edges[next]

            # the last element doesn't have to be the first element (it can be -1, too)
            if next in path:
                result = max(result, step - path[next])

        return result
