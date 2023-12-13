class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        height = len(mat)
        width  = len(mat[0])

        x = [ 0 ] * width
        y = [ 0 ] * height
        for j in range(len(mat)):
            y[j] = sum(mat[j])
            for i in range(len(mat[j])):
                x[i] += mat[j][i]

        result = 0
        for j in range(len(mat)):
            if y[j] == 1:
                for i in range(len(mat[j])):
                    if mat[j][i] == 1 and x[i] == 1:
                        result += 1
        return result
