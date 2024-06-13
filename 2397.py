class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        result = 0
        height = len(matrix)
        width  = len(matrix[0])

        zeros = 0
        # represent each row as a number
        compact = []
        for y in range(height):
            have = sum( m << i for i, m in enumerate(matrix[y]) )
            if have == 0:
                zeros += 1 # remove zeros, add them to our result in the final step
            else:
                compact.append(have)

        # iterate over all combinations
        all = list(range(width))
        for choose in combinations(all, numSelect):
            # bitmask of combination
            have = sum(1 << c for c in choose)

            # no bit set outside the mask
            valid  = sum(((have | row) == have) for row in compact)

            result = max(result, valid)
            if result == len(compact): # early exit
                break

        return zeros + result
