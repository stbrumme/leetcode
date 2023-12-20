class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        result = 0

        edges = defaultdict(list)
        for a, b in roads:
            edges[a].append(b)
            edges[b].append(a)

        def deeper(node, parent):
            passengers = 1           # representative of this city
            for next in edges[node]: # car sharing with "sub" city
                if next != parent:
                    passengers += deeper(next, node)

            # drive closer to capital city
            if node != 0:
                nonlocal result
                result += (passengers + seats - 1) // seats

            return passengers

        deeper(0, 0)
        return result
