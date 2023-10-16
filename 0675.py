class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        width  = len(forest[0])
        height = len(forest)

        # add all trees to min-heap
        trees = []
        for y in range(height):
            for x in range(width):
                if forest[y][x] > 1:
                    heappush(trees, (forest[y][x], x, y))

        steps = 0
        todo = [ ( 0, 0 ) ]
        while trees:
            # next tree
            th, tx, ty = heappop(trees)

            seen = set()
            cut  = False
            while todo and not cut:
                next = []
                for x, y in todo:
                    if x == tx and y == ty:
                        cut = True
                        next = [ (x, y) ]
                        forest[y][x] = 1
                        break

                    if forest[y][x] == 0:
                        continue

                    if (x, y) in seen:
                        continue
                    seen.add((x, y))

                    if x > 0:
                        next.append((x - 1, y))
                    if x < width - 1:
                        next.append((x + 1, y))
                    if y > 0:
                        next.append((x, y - 1))
                    if y < height - 1:
                        next.append((x, y + 1))

                if not cut:
                    steps += 1
                todo   = next

            if not cut:
                return -1

        return steps
