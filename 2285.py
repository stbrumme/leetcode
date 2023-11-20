class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        # idea: assign high values to cities that have many roads
        result = 0

        freq = { i: 0 for i in range(n) }
        for a, b in roads:
            freq[a] += 1
            freq[b] += 1

        cities = [ ( freq[f], f ) for f in freq ]
        id = 1
        for numroads, city in sorted(cities):
            result += id * numroads
            id     += 1

        return result
