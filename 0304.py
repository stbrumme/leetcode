class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        # 2D prefix sum
        for y in range(len(matrix)):
            for x in range(1, len(matrix[0])):
                matrix[y][x] += matrix[y][x-1]
        for y in range(1, len(matrix)):
            for x in range(len(matrix[0])):
                matrix[y][x] += matrix[y-1][x]
        self.prefix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result  = self.prefix[row2][col2] # full area
        if row1 > 0:
            result -= self.prefix[row1 - 1][col2] # minus left
        if col1 > 0:
            result -= self.prefix[row2][col1 - 1] # minus upper
        if row1 > 0 and col1 > 0:
            result += self.prefix[row1 - 1][col1 - 1] # upper-left was subtracted twice
        return result