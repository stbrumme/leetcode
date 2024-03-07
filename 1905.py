class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        height = len(grid1)
        width  = len(grid1[0])

        # replace +1 by ID
        def deeper(grid, x, y, id):
            # water or already assigned
            if grid[y][x] != 1:
                return

            grid[y][x] = id

            # recursion
            if x > 0:
                deeper(grid, x - 1, y, id)
            if x + 1 < width:
                deeper(grid, x + 1, y, id)
            if y > 0:
                deeper(grid, x, y - 1, id)
            if y + 1 < height:
                deeper(grid, x, y + 1, id)

        # find all islands in grid1 and assign a unique ID
        id = 2 # 1 is already used
        for y in range(height):
            for x in range(width):
                deeper(grid1, x, y, id)
                if grid1[y][x] == id:
                    id += 1

        # repeat for grid2
        id = 2 # 1 is already used
        for y in range(height):
            for x in range(width):
                deeper(grid2, x, y, id)
                if grid2[y][x] == id:
                    id += 1

        # map grid2 to grid1
        cover = defaultdict(set)
        for y in range(height):
            for x in range(width):
                one = grid1[y][x]
                two = grid2[y][x]
                if two != 0:
                    cover[two].add(one)

        result = 0
        for c in cover:
            if 0 in cover[c]:      # not entirely covered, there's some water
                continue
            if len(cover[c]) == 1: # covered by exactly one island
                result += 1

        return result
