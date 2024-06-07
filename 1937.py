class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        width = len(points[0])

        best  = [ 0 ] * width
        for row in points:
            one = [ 0 ] * width # maximum when looking left
            two = [ 0 ] * width # maximum when looking right

            one[0]  = best[0]
            two[-1] = best[-1]

            for x in range(1, width):
                # each cell's optimum is either the cell itself
                # or the optimum of its immediate neighbor minus one

                # left
                one[x]  = max(one[x  - 1] - 1, best[x])

                # right (reverse order)
                x2 = width - x - 1
                two[x2] = max(two[x2 + 1] - 1, best[x2])

            # choose best of both
            best = [ max(a, b) + value for a, b, value in zip(one, two, row) ]

        return max(best)
