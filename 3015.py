class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        # 0-based indexing is easier to handle
        x -= 1
        y -= 1

        matrix = [ [ n ] * n for _ in range(n) ]

        # identity
        for i in range(n):
            matrix[i][i] = 0
        # right neighbor
        for i in range(n - 1):
            matrix[i][i + 1] = 1
            matrix[i + 1][i] = 1
        # left  neighbor
        for i in range(1, n):
            matrix[i][i - 1] = 1
            matrix[i - 1][i] = 1

        # fast travel
        if x != y:
            matrix[x][y] = 1
            matrix[y][x] = 1

        # Floyd-Warshall
        for k in range(n):
            for i in range(n):
                for j in range(i + 1, n):
                    matrix[i][j] = matrix[j][i] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

        # count all distances
        result = [ 0 ] * n
        for i in range(n):
            for j in range(i + 1, n):     # process only i > j
                distance = matrix[i][j]
                result[distance - 1] += 2 # compensate for my i > j restriction

        return result
