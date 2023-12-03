class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        neighbors = defaultdict(list)
        for (a, b), p in zip(edges, succProb):
            neighbors[a].append(( p, b ))
            neighbors[b].append(( p, a ))

        done = set()
        todo = [ ( -1, start_node ) ] # max-heap
        while todo:
            p, node = heappop(todo)
            if node == end_node:
                return -p

            if node in done:
                continue
            done.add(node)

            for success, next in neighbors[node]:
                heappush(todo, ( p * success, next ))

        return 0
