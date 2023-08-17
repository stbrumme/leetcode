class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        width  = len(mat[0])
        height = len(mat)
        dist = [[99999 for i in range(width)] for j in range(height)]
        todo = []
        for y in range(height):
            for x in range(width):
                if mat[y][x] == 0:
                    dist[y][x] = 0
                    todo.append([y, x])

        iteration = 0
        while todo:
            iteration += 1
            process = todo
            todo = []
            for (y, x) in process:
                if x > 0 and dist[y][x-1] > iteration:
                    dist[y][x-1] = iteration
                    todo.append([y, x-1])
                if y > 0 and dist[y-1][x] > iteration:
                    dist[y-1][x] = iteration
                    todo.append([y-1, x])
                if x < width-1  and dist[y][x+1] > iteration:
                    dist[y][x+1] = iteration
                    todo.append([y, x+1])
                if y < height-1 and dist[y+1][x] > iteration:
                    dist[y+1][x] = iteration
                    todo.append([y+1, x])

        return dist
