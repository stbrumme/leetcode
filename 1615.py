class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        all = defaultdict(set)

        for i in roads:
            a = i[0]
            b = i[1]
            all[a].add(b)
            all[b].add(a)

        best = 0
        cities = sorted(all.keys())
        for i in range(len(cities)):
            for j in range(i+1, len(cities)):
                x = cities[i]
                y = cities[j]

                sum = len(all[x]) + len(all[y])
                if y in all[x]:
                    sum -= 1

                if best < sum:
                    best = sum

        return best
