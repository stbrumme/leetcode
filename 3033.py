class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        height = len(matrix)
        width  = len(matrix[0])
        for x in range(width):
            high = max(matrix[y][x] for y in range(height))
            for y in range(height):
                if matrix[y][x] == -1:
                    matrix[y][x] = high
        return matrix
