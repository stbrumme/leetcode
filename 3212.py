class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        result = 0
        height = len(grid)
        width  = len(grid[0])

        # count X & Y per row
        x = [ 0 ] * width
        y = [ 0 ] * width
        for row in grid:
            # current row
            newX = 0
            newY = 0

            for i, cell in enumerate(row):
                c = ord(cell)
                if   c == 88: # "X"
                    newX += 1
                elif c == 89: # "Y"
                    newY += 1

                x[i] += newX
                y[i] += newY

                result += x[i] and (x[i] == y[i])

        return result
