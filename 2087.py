class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        # my initial thought was some path-finding algorithm
        # but in the end it doesn't matter what path we take
        # because all paths are equal as long as they move through the same rows and same columns
        # shortest path is optimal => "never move away from home"

        y1, x1 = startPos
        y2, x2 = homePos

        cols = sum(colCosts[x1 + 1 : x2 + 1]) if x1 < x2 else sum(colCosts[x2 : x1])
        rows = sum(rowCosts[y1 + 1 : y2 + 1]) if y1 < y2 else sum(rowCosts[y2 : y1])
        return cols + rows
