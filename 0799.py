class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # store how much champagne was poured into each glass,
        # including everything that spilled over
        row = [ poured ]
        for i in range(query_row):
            next = [ 0.5 * max(0, row[0] - 1) ] # all but 1 unit overflows, 50% to each side
            for j in range(i):
                next.append(0.5 * max(0, row[j] - 1) + 0.5 * max(0, row[j + 1] - 1))
            next.append(next[0]) # right-most glass is identical to left-most
                                 # actually all glasses on the right half are
                                 # identical to the left half
                                 # so we could save roughly 50% of computations
            row = next

        result = row[query_glass]
        return min(result, 1) # return at most 1, the rest spilled over
