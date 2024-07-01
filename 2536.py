class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        size = n

        result = []
        for i in range(size):
            result.append([ 0 ] * (size + 1))

        # pass 1: set deltas
        for y1, x1, y2, x2 in queries:
            for y in range(y1, y2 + 1):
                result[y][x1]     += 1
                result[y][x2 + 1] -= 1

        # pass 2: convert deltas to absolute values
        for y in range(size):
            result[y] = list(accumulate(result[y]))
            result[y].pop()

        return result
