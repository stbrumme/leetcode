class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        width  = len(land[0])
        height = len(land)

        seen = set()
        for y in range(height):
            for x in range(width):
                # already processed
                if (x, y) in seen:
                    continue

                # forest
                if land[y][x] == 0:
                    continue

                # scan rectangle area
                maxx = width
                maxy = height
                for y2 in range(y, maxy):
                    if land[y2][x] == 0:
                        maxy = y2
                        break

                    for x2 in range(x, maxx):
                        if land[y2][x2] == 0:
                            maxx = x2
                            break
                        seen.add((x2, y2))

                yield y, x, maxy - 1, maxx - 1
