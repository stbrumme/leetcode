class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        height = len(matrix)
        width  = len(matrix[0])

        # str => int
        for y in range(height):
            for x in range(width):
                matrix[y][x] = int(matrix[y][x])

        # prefix sum
        for y in range(height):
            for x in range(1, width):
                if matrix[y][x] != 0 and matrix[y][x-1] != 0:
                    matrix[y][x] += matrix[y][x-1]

        result = 0
        for x in range(width):
            for y in range(height):
                w = width
                h = 0
                for scan in range(y, height):
                    if matrix[scan][x] == 0:
                        break
                    w  = min(w, matrix[scan][x])
                    h += 1
                    result = max(result, w*h)

        return result
