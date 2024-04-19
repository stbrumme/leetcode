class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        height = len(mat)
        width  = len(mat[0])

        # all numbers encountered along the way
        have = defaultdict(int)

        # 8 directions
        delta = [ [ +1, +1 ], [ +1, 0 ], [ +1, -1 ], \
                  [  0, +1 ],            [  0, -1 ], \
                  [ -1, +1 ], [ -1, 0 ], [ -1, -1 ] ]

        # traverse all cells
        for y in range(height):
            for x in range(width):
                for dx, dy in delta:
                    # traverse all paths
                    value = 0
                    xx = x
                    yy = y
                    while 0 <= xx < width and 0 <= yy < height:
                        value *= 10
                        value += mat[yy][xx]
                        if value > 10 and value & 1: # basic test to reject even numebrs
                            have[value] += 1

                        xx += dx
                        yy += dy

        # sort by frequency (reverse: most frequent first, prefer higher number)
        candidates = [ ( howoften, value ) for value, howoften in have.items() ]
        for howoften, value in sorted(candidates, reverse = True):
            prime = True
            # check if prime (even numbers were already filtered above)
            for factor in count(3, 2):
                if factor * factor > value:
                    break
                if value % factor == 0:
                    prime = False
                    break

            # done !
            if prime:
                return value

        return -1 # failed
