class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        all = defaultdict(dict)
        for i in range(len(equations)):
            a, b = equations[i]
            c    = values[i]
            all[a][b] = c
            all[b][a] = 1 / c

        again = True
        while again:
            again = False
            derived = defaultdict(dict)
            for one in all:
                for two in sorted(all[one]):
                    for three in sorted(all[one]):
                        if two < three and three not in all[two]:
                            x = all[one][two]
                            y = all[one][three]
                            derived[two][three] = y / x
                            derived[three][two] = x / y
                            again = True

            for x in derived:
                for y in derived[x]:
                    all[x][y] = derived[x][y]

        result = []
        for a, b in queries:
            if a in all and b in all[a]:
                result.append(all[a][b])
            elif a == b and a in all:
                result.append(1)
            else:
                result.append(-1)
        return result
