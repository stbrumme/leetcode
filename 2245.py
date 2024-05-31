class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        result = 0

        height = len(grid)
        width  = len(grid[0])

        # 10 = 2 * 5, any other prime factor doesn't matter
        # create tuples (a, b) where a is the number of 2s and b the number of 5s
        tens = []
        for y in range(height):
            tens.append([])
            for x in range(width):
                current = grid[y][x]

                two  = 0
                while (current & 1) == 0: # same as x & 1 == x % 2
                    current //= 2
                    two      += 1

                five = 0
                while current % 5 == 0:
                    current //= 5
                    five     += 1

                tens[-1].append(( two, five ))

        # pairwise additions tuples of size 2
        def add(one, two, three = ( 0,0 )): # third paramter is optional
            return ( one[0] + two[0] + three[0], one[1] + two[1] + three[1] )

        # let's abuse Python's caching ... dedicated lists/tables might be faster, though
        @cache
        def left(x, y):
            return ( 0, 0 ) if x <  0      else add(tens[y][x], left (x - 1, y))
        @cache
        def right(x, y):
            return ( 0, 0 ) if x == width  else add(tens[y][x], right(x + 1, y))
        @cache
        def up(x, y):
            return ( 0, 0 ) if y <  0      else add(tens[y][x], up   (x, y - 1))
        @cache
        def down(x, y):
            return ( 0, 0 ) if y == height else add(tens[y][x], down (x, y + 1))

        for y in range(height):
            for x in range(width):
                a = add(tens[y][x], left (x - 1, y), up  (x, y - 1))
                b = add(tens[y][x], left (x - 1, y), down(x, y + 1))
                c = add(tens[y][x], right(x + 1, y), up  (x, y - 1))
                d = add(tens[y][x], right(x + 1, y), down(x, y + 1))

                # number of zeros is based on pairs 2 * 5
                # whatever we have the least determines the number of zeros
                result = max(result, min(a), min(b), min(c), min(d))

        return result
