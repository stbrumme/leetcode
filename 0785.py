class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        a = set([ 0 ])
        b = set()

        todo = [ 0 ]
        done = set()
        while todo:
            i = todo.pop()
            if i not in done:
                done.add(i)

                for g in graph[i]:
                    if i in a:
                        b.add(g)
                    else:
                        a.add(g)

                    if g in a and g in b:
                        return False # a node must never belong to both sets
                    todo.append(g)

            # choose next seed value if graph is split
            if not todo:
                for i in range(len(graph)):
                    if i not in done:
                        a.add(i)
                        todo.append(i)
                        break

        return True
