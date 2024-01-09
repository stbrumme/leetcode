class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        width  = len(matrix[0])
        height = len(matrix)

        # lucky column
        col = []
        for x in range(width):
            col.append(max(m[x] for m in matrix))

        for y in range(height):
            # lucky row
            lucky = min(matrix[y])
            for x in range(width):
                if matrix[y][x] == lucky and lucky == col[x]:
                    yield lucky
