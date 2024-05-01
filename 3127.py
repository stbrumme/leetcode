class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        def white(x, y):
            return (grid[y    ][x] == "W") + (grid[y    ][x + 1] == "W") + \
                   (grid[y + 1][x] == "W") + (grid[y + 1][x + 1] == "W")

        return white(0, 0) != 2 or white(0, 1) != 2 or \
               white(1, 0) != 2 or white(1, 1) != 2
