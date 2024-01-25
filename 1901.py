class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        width  = len(mat[0])
        height = len(mat)

        restart = width # quite arbitrary choice
        while True:
            # start at any point
            x = randint(0, width  - 1)
            y = randint(0, height - 1)

            # abort search if not successful (but longer searches in next iteration)
            for step in range(restart):
                value = mat[y][x]

                # if there is a greater neighbor, then continue with that cell
                if x > 0          and mat[y][x - 1] > value:
                    x -= 1
                    continue
                if x < width - 1  and mat[y][x + 1] > value:
                    x += 1
                    continue
                if y > 0          and mat[y - 1][x] > value:
                    y -= 1
                    continue
                if y < height - 1 and mat[y + 1][x] > value:
                    y += 1
                    continue

                return y, x

            restart += width
