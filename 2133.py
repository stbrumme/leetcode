class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)

        # horizontal
        for y in range(n):
            if min(matrix[y]) != 1 or max(matrix[y]) != n or len(set(matrix[y])) != n:
                return False

        # vertical
        for x in range(n):
            col = []
            for y in range(n):
                col.append(matrix[y][x])
            if min(col) != 1 or max(col) != n or len(set(col)) != n:
                return False

        return True
