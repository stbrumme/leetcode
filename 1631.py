class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        width  = len(heights[0])
        height = len(heights)

        effort = []
        for _ in range(height):
            effort.append([ 9999999999 ] * width)
        effort[height-1][width-1] = 0

        todo = [ [ width-1, height-1 ] ]
        while todo:
            next = []
            for x, y in todo:
                if x > 0:
                    path = max(effort[y][x], abs(heights[y][x-1] - heights[y][x]))
                    if effort[y][x-1] > path:
                        effort[y][x-1] = path
                        next.append([ x-1, y ])
                if x < width-1:
                    path = max(effort[y][x], abs(heights[y][x+1] - heights[y][x]))
                    if effort[y][x+1] > path:
                        effort[y][x+1] = path
                        next.append([ x+1, y ])
                if y > 0:
                    path = max(effort[y][x], abs(heights[y-1][x] - heights[y][x]))
                    if effort[y-1][x] > path:
                        effort[y-1][x] = path
                        next.append([ x, y-1 ])
                if y < height-1:
                    path = max(effort[y][x], abs(heights[y+1][x] - heights[y][x]))
                    if effort[y+1][x] > path:
                        effort[y+1][x] = path
                        next.append([ x, y+1 ])
            
            todo = next

        return effort[0][0]