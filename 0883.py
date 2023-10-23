class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        xy = set()
        xz = set()
        yz = set()
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                height = grid[y][x]
                for z in range(height):
                    xy.add((x, y))
                    xz.add((x, z))
                    yz.add((y, z))
        return len(xy) + len(xz) + len(yz)
