class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)

        for _ in range(4): # compare original matrix and three rotations (90, 180, 270 degrees)
            match = True
            for y in range(n):
                for x in range(n):
                    match &= mat[y][x] == target[y][x]
            if match:
                return True

            # rotate by 90 degrees
            rotated = []
            for _ in range(n):
                rotated.append([ -1 ] * n)
            for x in range(n):
                for y in range(n):
                    rotated[y][x] = mat[x][n - y - 1]
            mat = rotated

        return False
