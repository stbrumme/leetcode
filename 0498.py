class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        width  = len(mat[0])
        height = len(mat)

        dx = +1
        dy = -1
        x  = 0
        y  = 0

        result = []
        while x != width - 1 or y != height - 1:
            result.append(mat[y][x])

            x += dx
            y += dy

            if x == width:
                x -= 1
                y += 2
                dx, dy = dy, dx

            if y == height:
                x += 2
                y -= 1
                dx, dy = dy, dx

            if x < 0 or y < 0:
                x = max(x, 0)
                y = max(y, 0)
                dx, dy = dy, dx

        result.append(mat[height - 1][width - 1])
        return result
