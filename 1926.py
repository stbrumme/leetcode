class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        width  = len(maze[0])
        height = len(maze)

        y, x = entrance
        todo = [ [ x, y ] ]

        steps = 0
        while todo:
            next = []

            for x, y in todo:
                # already blocked ?
                if maze[y][x] != ".":
                    continue

                if x == 0 or y == 0 or x == width-1 or y == height-1:
                    if steps > 0: # entrance must not be an exit
                        return steps

                # block current cell
                maze[y][x] = "o"

                # one-based
                if x < width - 1  and maze[y][x+1] == ".":
                    next.append([ x+1, y ])
                if x > 0          and maze[y][x-1] == ".":
                    next.append([ x-1, y ])
                if y > 0          and maze[y-1][x] == ".":
                    next.append([ x, y-1 ])
                if y < height - 1 and maze[y+1][x] == ".":
                    next.append([ x, y+1 ])

            steps += 1
            todo = next

        return -1
