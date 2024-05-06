class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        result = 0

        height = len(matrix)
        width  = len(matrix[0])

        # row-wise prefix sum (in situ)
        for m in matrix:
            for x in range(1, width):
                m[x] += m[x - 1]

        for left in range(width):
            for right in range(left, width):
                have = { 0: 1 } # properly catch rectangles starting in the first column

                prefix = 0 # vertical prefix sum
                for y in range(height):
                    # sliding window
                    prefix += matrix[y][right]
                    prefix -= matrix[y][left - 1] if left > 0 else 0

                    need         = prefix - target
                    result      += have.get(need,   0)
                    have[prefix] = have.get(prefix, 0) + 1

        return result
