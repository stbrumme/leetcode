class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        width  = len(grid[0])
        height = len(grid)

        # breadth first search
        open = set() # unknown cells
        todo = set() # current "wavefront", initially all land cells
        for y in range(height):
            for x in range(width):
                if grid[y][x] == 0:
                    open.add(( x, y ))
                else:
                    todo.add(( x, y ))

        # only water or only land
        if not open or not todo:
            return -1

        distance = 0
        while open:
            next = set()
            for x, y in todo:
                if ( x + 1, y ) in open:
                    next.add(( x + 1, y ))
                if ( x - 1, y ) in open:
                    next.add(( x - 1, y ))
                if ( x, y + 1 ) in open:
                    next.add(( x, y + 1 ))
                if ( x, y - 1 ) in open:
                    next.add(( x, y - 1 ))

            open -= next
            todo  = next
            distance += 1

        return distance
