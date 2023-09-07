class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left  = 0
        right = len(matrix[0])
        for y in range(len(matrix)):
            if matrix[y][-1] < target:
                continue

            pos = bisect_right(matrix[y], target, left, right)
            print(pos, y)
            if pos == 0 and matrix[y][0] > target:
                return False
            if pos > 0 and matrix[y][pos - 1] == target:
                return True

            right = pos

        return False
