class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        x = cStart
        y = rStart

        deltas = [ [ +1, 0], [ 0, +1 ], [ -1, 0 ], [ 0, -1] ]
        direction = 0
        dx, dy = deltas[direction]

        steps  = 1
        xsteps = ysteps = steps

        found = 0
        size  = rows * cols
        while found < size:
            if 0 <= x < cols and 0 <= y < rows:
                yield y, x # row, col
                found += 1

            if dx != 0:
                x += dx
                xsteps -= abs(dx)
                if xsteps == 0:
                    direction += 1
                    dx, dy = deltas[direction]
                    steps += 1
                    xsteps = steps
            else: # dy != 0
                y += dy
                ysteps -= abs(dy)
                if ysteps == 0:
                    direction = (direction + 1) & 3
                    dx, dy = deltas[direction]
                    ysteps = steps
