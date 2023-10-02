class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        target = len(graph) - 1

        def deeper(node, have):
            next = have.copy() + [ node ]
            if node == target:
                result.append(next)
            else:
                for g in graph[node]:
                    deeper(g, next)

        deeper(0, [])
        return result
