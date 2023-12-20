class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        size = len(grid)

        # start in upper-left corner
        if grid[0][0] != 0:
            return False

        moves = []
        for y in range(size):
            for x in range(size):
                moves.append(( grid[y][x], x, y))
        moves.sort() # ordered by move number

        for i in range(1, len(moves)):
            # verify move number
            if moves[i][0] != moves[i - 1][0] + 1:
                return False

            # 2 step into one direction and 1 in another
            dx = abs(moves[i][1] - moves[i - 1][1])
            dy = abs(moves[i][2] - moves[i - 1][2])
            if dx + dy != 3 or dx * dy != 2:
                return False

        return True
