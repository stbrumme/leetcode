class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        width  = len(isWater[0])
        height = len(isWater)

        # identify all water cells
        # convert water from +1 to 0 and land from 0 to -1
        unknown = -1
        todo = set()
        for y in range(height):
            for x in range(width):
                if isWater[y][x] == 1:
                    todo.add((x, y))
                    isWater[y][x] = 0
                else:
                    isWater[y][x] = unknown

        seen  = set()
        level = 0 # water
        while todo:
            next = set()

            for x, y in todo:
                if (x, y) in seen:
                    continue
                seen.add((x, y))
                isWater[y][x] = level

                if x > 0 and isWater[y][x - 1] == unknown:
                    next.add((x - 1, y))
                if y > 0 and isWater[y - 1][x] == unknown:
                    next.add((x, y - 1))
                if x < width - 1  and isWater[y][x + 1] == unknown:
                    next.add((x + 1, y))
                if y < height - 1 and isWater[y + 1][x] == unknown:
                    next.add((x, y + 1))

            todo   = next
            level += 1
        return isWater
