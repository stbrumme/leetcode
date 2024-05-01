class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        result = [ -1 ] * n

        graph = [ [] for _ in range(n) ]
        for u, v, length in edges:
            graph[u].append(( v, length ))
            graph[v].append(( u, length ))

        # expected visiting time
        expect = [ +inf ] * n

        todo = [ ( 0, 0 ) ] # min-heap: ( time, node )
        while todo:
            now, node = heappop(todo)

            # already processed
            if result[node] != -1:
                continue

            # yeah, reached a new node
            result[node] = now

            # continue with adjacent nodes
            for next, duration in graph[node]:
                arrive = now + duration
                if arrive < min(expect[next], disappear[next]):
                    heappush(todo, ( arrive, next ))
                    expect[next] = arrive

        return result
