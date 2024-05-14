class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        result = +inf

        size = len(grid)
        half = size // 2

        def why(x, y): # True if part of the letter Y
            if y < half: # upper half: twp diagonals
                return x == y or x == size - y - 1
            else:        # lower half: one vertical line
                return x == half

        inside  = defaultdict(int) # numbers belongs to Y
        outside = defaultdict(int) # numbers not in Y
        for y in range(size):
            for x in range(size):
                value = grid[y][x]
                if why(x, y):
                    inside[value]  += 1
                else:
                    outside[value] += 1

        # only one number on the whole grid
        if len(inside) == 1 and len(inside | outside) == 1:
            return sum(inside.values()) # Y always covers less cells than its outside
                                        # paint all Y cell in a new color

        a = sorted([ ( -value, key ) for key, value in inside .items() ])
        b = sorted([ ( -value, key ) for key, value in outside.items() ])

        # pick the most frequent numbers but avoid collisions
        for countA, numA in a[ : 2]:     # sufficient to check the 2 most frequent
            for countB, numB in b[ : 2]:
                if numA != numB:
                    changeIn  = sum(inside .values()) + countA # count was negated, therefore add
                    changeOut = sum(outside.values()) + countB
                    result    = min(result, changeIn + changeOut)

        return result
