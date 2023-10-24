class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        width  = len(grid[0])
        height = len(grid)

        def ismagic(x, y):
            # must be 9 distinct numbers
            unique = set()
            for j in range(3):
                for i in range(3):
                    unique.add(grid[y + j][x + i])
            # I got the next three checks from the discussion only, they are not obvious from the problem statement
            if len(unique) != 9:
                return False
            if min(unique) != 1:
                return False
            if max(unique) != 9:
                return False

            h1 = grid[y    ][x    ] + grid[y    ][x + 1] + grid[y    ][x + 2]
            h2 = grid[y + 1][x    ] + grid[y + 1][x + 1] + grid[y + 1][x + 2]
            h3 = grid[y + 2][x    ] + grid[y + 2][x + 1] + grid[y + 2][x + 2]
            v1 = grid[y    ][x    ] + grid[y + 1][x    ] + grid[y + 2][x    ]
            v2 = grid[y    ][x + 1] + grid[y + 1][x + 1] + grid[y + 2][x + 1]
            v3 = grid[y    ][x + 2] + grid[y + 1][x + 2] + grid[y + 2][x + 2]
            d1 = grid[y    ][x    ] + grid[y + 1][x + 1] + grid[y + 2][x + 2]
            d2 = grid[y    ][x + 2] + grid[y + 1][x + 1] + grid[y + 2][x    ]
            return h1 == h2 and h2 == h3 and h3 == v1 and v1 == v2 and v2 == v3 and v3 == d1 and d1 == d2

        result = 0
        for y in range(height - 2):
            for x in range(width - 2):
                if ismagic(x, y):
                    result += 1

        return result
