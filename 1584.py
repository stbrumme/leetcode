class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Manhattan distance
        def cost(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            return abs(x2 - x1) + abs(y2 - y1)

        class Edge:
            def __init__(self, p1, p2):
                self.one = p1
                self.two = p2
                self.distance = cost(points[p1], points[p2])

            def __lt__(self, other):
                return self.distance < other.distance

        # modified Prim's algorithm
        size  = len(points)
        inside  = set([ 0 ])
        outside = set(range(1, size))

        next    = []
        for i in outside:
            heappush(next, Edge(0, i))

        result  = 0
        while outside:
            add = next[0]
            while add.one in inside and add.two in inside:
                heappop(next)
                add = next[0]

            inside .add   (add.two)
            outside.remove(add.two)
            result += add.distance

            for i in outside:
                heappush(next, Edge(add.two, i))

        return result
