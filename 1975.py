class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        height = len(matrix)
        width  = len(matrix[0])

        # connect all negative numbers like the snake game
        # (there could be many positive numbers inbetween)
        # and keep flipping the sign between each pair of neighbors

        # in the end at most one negative number remains
        # case A: no  negative number left
        # case B: one negative number left
        #         make sure that it's as close as possible to zero
        #         in some inputs it makes sense to make a positive number negative and a negative positive
        # zero is a special case: we can always flip its sign
        # hence if there's at least one zero, no negative number will remain
        last  = +inf
        count = 0     # count negative numbers
        zeros = False # True, if at least one zero
        total = 0     # absolute sum of all numbers
        for y in range(height):
            for x in range(width):
                value  = matrix[y][x]
                total += abs(value)
                last   = min(last, abs(value))
                if   value <  0:
                    count += 1
                elif value == 0:
                    zeros  = True

        # no negative left
        if (count & 1) == 0 or zeros:
            last = 0

        return total - 2 * last # the last negative number was added as a positive number
                                # so we need to correct for that mistake
                                # however, it has a negative sign, therefore add
