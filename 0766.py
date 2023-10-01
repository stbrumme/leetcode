class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for y in range(1, len(matrix)):
            for x in range(1, len(matrix[0])):
                if matrix[y][x] != matrix[y-1][x-1]:
                    return False
        return True
