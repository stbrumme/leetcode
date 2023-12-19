class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        all = []
        for r in range(rows):
            for c in range(cols):
                dr = abs(cCenter - c)
                dc = abs(rCenter - r)
                all.append(( dr + dc, r, c ))

        return [ [ r, c ] for d, r, c in sorted(all) ]
