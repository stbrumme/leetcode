class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        connect = [ [] for _ in range(n) ]
        for a, b in edges:
            connect[a].append(b)
            connect[b].append(a)

        todo = [ source ]
        seen = [ False ] * n
        while todo:
            pos = todo.pop()
            if pos == destination:
                return True

            if seen[pos]:
                continue
            seen[pos] = True

            todo.extend(connect[pos])

        return False
