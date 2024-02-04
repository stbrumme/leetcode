class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        size = len(grid)
        for y in range(size):
            for x in range(size):
                diagonal = (x == y or x == size - y - 1)
                positive = (grid[y][x] != 0)
                if diagonal ^ positive:
                    return False
        return True
