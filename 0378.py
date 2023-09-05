class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        heap = []

        result = matrix[0][0]
        next = [0] * n
        next[0] += 1

        while k > 1:
            low = 99999999999
            ymin = 0
            for y in range(len(next)):
                x = next[y]
                if x < n and low > matrix[y][x]:
                    low = matrix[y][x]
                    ymin = y

            result = low
            next[ymin] += 1
            k -= 1

        return result
