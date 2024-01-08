class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        width  = len(matrix[0])
        height = len(matrix)

        # 1x1 in first row
        result = sum(matrix[0])
        for y in range(1, height):
            # 1x1 in first column
            result += matrix[y][0]
            # everything else
            for x in range(1, width):
                # smallest square on top/left/topleft side
                a = matrix[y - 1][x - 1]
                b = matrix[y - 1][x    ]
                c = matrix[y    ][x - 1]
                # grow it by one
                count = 1 + min(a, b, c)
                # little trick: stays zero or becomes the lowest of a,b,c
                matrix[y][x] *= count

                # count all of them
                result += matrix[y][x]

        return result
