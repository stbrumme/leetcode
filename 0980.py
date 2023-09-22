class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        width  = len(grid[0])
        height = len(grid)

        result = 0

        def id(x, y):
            return 1 << (x + width * y)

        initmask = 0
        finish   = 0
        startx, starty = -1, -1
        lastx,  lasty  = -1, -1
        for y in range(height):
            for x in range(width):
                if grid[y][x] == 1:
                    initmask |= id(x, y)
                    startx = x
                    starty = y
                if grid[y][x] == 2:
                    lastx = x
                    lasty = y
                if grid[y][x] != -1:
                    finish |= id(x, y)

        def deeper(x, y, have):
            if x == lastx and y == lasty:
                if have == finish:
                    nonlocal result
                    result += 1
                return
            
            if x < 0 or y < 0 or x >= width or y >= height:
                return

            if x > 0          and not (id(x-1, y) & have):
                deeper(x-1, y, have | id(x-1, y))
            if x < width - 1  and not (id(x+1, y) & have):
                deeper(x+1, y, have | id(x+1, y))
            if y > 0          and not (id(x, y-1) & have):
                deeper(x, y-1, have | id(x, y-1))
            if y < height - 1 and not (id(x, y+1) & have):
                deeper(x, y+1, have | id(x, y+1))
        
        deeper(startx, starty, initmask)
        return result