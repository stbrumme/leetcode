class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        width  = len(mat[0])
        height = len(mat)
        if width * height != r * c:
            return mat

        result = []
        for y in range(height):
            for x in range(width):
                if not result or len(result[-1]) == c:
                    result.append([])
                result[-1].append(mat[y][x])

        return result
