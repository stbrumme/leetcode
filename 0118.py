class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [ [1] ]
        for i in range(1, numRows):
            row = []
            for j in range(1, i):
                row.append(result[i - 1][j - 1] + result[i - 1][j])
            result.append([ 1 ] + row + [ 1 ])
        return result
