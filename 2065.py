class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        result = 0

        graph = defaultdict(list)
        for u, v, time in edges:
            graph[u].append(( v, time ))
            graph[v].append(( u, time ))

        def deeper(node, time, quality, path):
            # too long
            if time > maxTime:
                return

            # improve quality
            if node not in path:
                quality += values[node]

            # initial node
            if node == 0:
                nonlocal result
                result = max(result, quality)

            # keep searching
            for next, weight in graph[node]:
                deeper(next, time + weight, quality, path + [ node ])

        deeper(0, 0, 0, [])
        return result
