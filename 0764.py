class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        allx = defaultdict(list)
        ally = defaultdict(list)
        for m in mines:
            allx[m[0]].append(m[1])
            ally[m[1]].append(m[0])

        for a in allx:
            allx[a].sort()
        for a in ally:
            ally[a].sort()

        result = 0
        for x in range(n):
            for y in range(n):
                left  = -1
                right = n
                pos = bisect_left(ally[y], x)
                if pos < len(ally[y]):
                    right = ally[y][pos]
                if pos > 0:
                    left  = ally[y][pos - 1]

                if right == x or left == x:
                    continue

                gapx = min(abs(x - right), abs(x - left))

                top    = -1
                bottom = n
                pos = bisect_left(allx[x], y)
                if pos < len(allx[x]):
                    bottom = allx[x][pos]
                if pos > 0:
                    top    = allx[x][pos - 1]

                if top == y or bottom == y:
                    continue

                gapy = min(abs(y - top), abs(y - bottom))

                size   = min(gapx, gapy)
                result = max(result, size)

        return result
