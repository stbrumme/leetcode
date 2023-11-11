class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.nodes = defaultdict(list)
        self.costs = defaultdict(list)
        self.have  = set()
        for e in edges:
            self.addEdge(e)

    def addEdge(self, edge: List[int]) -> None:
        a, b, cost = edge
        self.nodes[a].append(b)
        self.costs[a].append(cost)
        self.have.add(a)
        self.have.add(b)

    def shortestPath(self, node1: int, node2: int) -> int:
        # basic breadth-first-search / Dijkstra
        # home is where the heart is
        if node1 == node2:
            return 0
        # impossible
        if node1 not in self.have or node2 not in self.have:
            return -1

        # min-heap
        todo = [ (0, node1) ]
        seen = set()
        while todo:
            cost, node = heappop(todo)

            # arrived
            if node == node2:
                return cost

            # have better route
            if node in seen:
                continue
            seen.add(node)

            # dead end
            if node not in self.nodes:
                continue

            # keep going
            for nextnode, nextcost in zip(self.nodes[node], self.costs[node]):
                if nextnode not in seen: # avoid loops
                    heappush(todo, ( cost + nextcost, nextnode ))

        return -1
