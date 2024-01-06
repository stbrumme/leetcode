class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        stop = set((x, y) for x, y in obstacles)

        x = y = 0
        deltas    = [ [ 0, +1 ], [ -1, 0 ], [ 0, -1 ], [ +1, 0 ] ]
        direction = 0

        result = 0
        for c in commands:
            # turn left
            if   c == -1:
                direction -= 1
                if direction == -1:
                    direction = 3
            # turn right
            elif c == -2:
                direction += 1
                if direction == 4:
                    direction = 0
            # move forward
            else:
                dx, dy = deltas[direction]
                for k in range(c):
                    if (x + dx, y + dy) in stop:
                        break

                    x += dx
                    y += dy

                result = max(result, x*x + y*y)

        return result
