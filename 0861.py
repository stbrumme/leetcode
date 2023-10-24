class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        width  = len(grid[0])
        height = len(grid)

        for y in range(height):
            if grid[y][0] == 0: # flip row
                for x in range(width):
                    grid[y][x] ^= 1

        # convert to integers
        scores = []
        for y in range(height):
            scores.append(0)
            for x in range(width):
                scores[y] <<= 1
                scores[y]  |= grid[y][x]

        # flip columns
        mask = 1 << width
        for x in range(width):
            flip = scores.copy()
            mask >>= 1
            for y in range(height):
                flip[y] ^= mask

            if sum(scores) < sum(flip):
                scores = flip

        return sum(scores)
