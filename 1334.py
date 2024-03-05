class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        unknown = 10**10
        # nxn matrix
        all = [ [ unknown ] * n for _ in range(n) ]

        # staying in the city
        for a in range(n):
            all[a][a] = 0

        for a, b, weight in edges:
            all[a][b] = weight
            all[b][a] = weight

        # modified Floyd-Warshall algorithm
        for mid in range(n):
            for a in range(n):
                if a != mid and all[a][mid] < unknown:
                    for b in range(a + 1, n): # process only a < b and mirror the result
                        all[a][b] = all[b][a] = min(all[a][b], all[a][mid] + all[mid][b])

        result = 0
        low    = n
        for i, row in enumerate(all):
            nearby = sum(1 for r in row if r <= distanceThreshold)
            # more "remote" than other cities
            if low >= nearby:
                low = nearby
                result = i

        return result
