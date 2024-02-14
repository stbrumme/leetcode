class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        height = len(mat)
        width  = len(mat[0])

        # create sorted list of all values
        all = defaultdict(list)
        for y in range(height):
            for x in range(width):
                value = mat[y][x]
                all[value].append(( x, y ))

        # all zeros
        best = [ [ 0 ] * width for y in range(height) ]
        cols = [ 0 ] * width
        rows = [ 0 ] * height

        # lowest values first (they have the shortest paths)
        for value in sorted(all):
            # update path length of all cells with the same values
            for x, y in all[value]:
                best[y][x] = 1 + max(cols[x], rows[y])

            # track longest paths per row/column
            for x, y in all[value]:
                cols[x] = max(cols[x], best[y][x])
                rows[y] = max(rows[y], best[y][x])

        return max(best[y][x] for x in range(width) for y in range(height))
