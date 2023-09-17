class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        width  = len(matrix[0])
        height = len(matrix)

        todo = set()
        for x in range(width):
            for y in range(height):
                todo.add(tuple([ x, y ]))

        longest = 0
        while todo:
            longest += 1
            next = set()
            for x,y in list(todo):
                current = matrix[y][x]
                if x > 0 and matrix[y][x-1] > current:
                    next.add(tuple([ x-1, y ]))
                if x < width - 1 and matrix[y][x+1] > current:
                    next.add(tuple([ x+1, y ]))
                if y > 0 and matrix[y-1][x] > current:
                    next.add(tuple([ x, y-1 ]))
                if y < height - 1 and matrix[y+1][x] > current:
                    next.add(tuple([ x, y+1 ]))

            todo = next        

        return longest