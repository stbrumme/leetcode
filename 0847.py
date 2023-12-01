class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        size = len(graph)

        # weird syntax for tuples of size 1 in Python
        todo = set([ ( i, )  for i in range(size) ])
        # the last item will be the current position

        # breadth-first search
        steps = 0
        while todo:
            steps += 1
            next   = set()

            for visited in todo:
                last    = visited[-1]
                history = set(visited)

                # visit all neighbors
                for follow in graph[last]:
                    have = tuple(history) + ( follow, )
                    # done ?
                    if len(history) == size - 1 and follow not in history:
                        return steps
                    next.add(have)

            todo = next

        return 0
