class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        height = len(mat)
        width  = len(mat[0])

        # not yet visited cells per column / row
        cols = [ height ] * width
        rows = [ width  ] * height

        # store location of each value in the matrix
        pos  = [ None ] * (height * width + 1)
        for y in range(height):
            for x in range(width):
                pos[mat[y][x]] = ( x, y )

        for i, a in enumerate(arr):
            # visit cell
            x, y = pos[a]
            cols[x] -= 1
            rows[y] -= 1
            # done ?
            if cols[x] == 0 or rows[y] == 0:
                return i
