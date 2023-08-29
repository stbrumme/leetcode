class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        for y in range(len(matrix) - 2, -1, -1):
            for x in range(len(matrix[y])):
                best = matrix[y+1][x]
                if x > 0:
                    best = min(best, matrix[y+1][x-1])
                if x < len(matrix[y]) - 1:
                    best = min(best, matrix[y+1][x+1])
                matrix[y][x] += best

        return min(matrix[0])
