class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        result = 0
        height = len(matrix)
        width  = len(matrix[0])

        # vertical prefix sum with reset if zero
        prefix = [ 0 ] * width

        # best horizontal combo
        for y in range(height):
            for x, bit in enumerate(matrix[y]):
                prefix[x] += 1
                prefix[x] *= bit # keeps value or resets to zero

            for dx, dy in enumerate(sorted(prefix, reverse = True), start = 1):
                result = max(result, dx * dy)

        return result
