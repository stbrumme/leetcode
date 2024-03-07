class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        height = len(mat)
        width  = len(mat[0])

        # 2D prefix sum
        prefix = mat.copy()
        for y in range(height):
            for x in range(1, width):
                prefix[y][x] += prefix[y][x - 1]
        for y in range(1, height):
            for x in range(width):
                prefix[y][x] += prefix[y - 1][x]

        result = [ [ 0 ] * width for _ in range(height) ]
        for y in range(height):
            for x in range(width):
                # prefix sums at each corners must be added/subtracted
                # ++++-----
                # ++++-----
                # ----+++++
                # ----+++++
                left  = x - k
                right = min(width - 1, x + k)
                up    = y - k
                down  = min(height - 1, y + k)

                total = prefix[down][right]
                if left > 0:
                    total -= prefix[down][left - 1]
                if up   > 0:
                    total -= prefix[up - 1][right]
                if left > 0 and up > 0:
                    total += prefix[up - 1][left - 1]

                result[y][x] = total

        return result
