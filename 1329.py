class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        width  = len(mat[0])
        height = len(mat)

        # assign each diagonal an ID
        getDiagonal = lambda x, y: y - x
        # store values of each diagonal
        diagonals = defaultdict(list)

        for y in range(height):
            for x in range(width):
                d = getDiagonal(x, y)
                diagonals[d].append(mat[y][x])

        for d in diagonals:
            diagonals[d].sort()

        for y in range(height):
            for x in range(width):
                d = getDiagonal(x, y)
                mat[y][x] = diagonals[d].pop(0)

        return mat
