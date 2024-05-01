class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        result = 0
        height = len(grid)
        width  = len(grid[0])

        prefix = [ 0 ] * width
        for y in range(height):
            row = 0
            for x in range(width):
                row       += grid[y][x]
                prefix[x] += row
                if prefix[x] > k:
                    break

                result += 1

        return result
