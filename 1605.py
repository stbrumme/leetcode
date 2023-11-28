class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        width  = len(colSum)
        height = len(rowSum)
        result = [ [ 0 ] * width for _ in range(height) ]

        for x in range(width):
            for y in range(height):
                # select the largest value such that colsum and rownum are still non-negative
                low = min(colSum[x], rowSum[y])
                result[y][x] = low
                colSum[x]   -= low
                rowSum[y]   -= low

        return result
