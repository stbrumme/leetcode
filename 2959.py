class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        result = 1 # closing all branches is a valid solution

        # default matrix with roads, before searching for shortest connections
        default = [ [ +inf ] * n for _ in range(n) ]
        for a, b, w in roads:
            default[a][b] = min(default[a][b], w) # there might be multiple roads between two cities
            default[b][a] = min(default[b][a], w)
        for a in range(n):
            default[a][a] = 0 # stay in a city

        combinations = 1 << n
        for mask in range(1, combinations):
            # get active branches from bitmask
            cities = [ i for i in range(n) if (1 << i) & mask ]

            # trivial cases
            if len(cities) == 1:
                result += 1
                continue

            # initial distances
            matrix = deepcopy(default)

            # Floyd-Warshall
            for mid in cities:
                for a in cities:
                    if a != mid:
                        for b in cities:
                            if a < b and b != mid:
                                matrix[a][b] = matrix[b][a] = min(matrix[a][b], matrix[a][mid] + matrix[mid][b])

            valid = 1
            for a in cities:
                if any(matrix[a][b] > maxDistance for b in cities if a > b):
                    valid = 0
                    break
            result += valid

        return result
