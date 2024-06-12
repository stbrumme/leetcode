class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        result = 0

        stockPrices.sort()
        dx1 = 0
        dy1 = +inf
        for (x1, y1), (x2, y2) in zip(stockPrices, stockPrices[1 :]):
            dx2 = x2 - x1
            dy2 = y2 - y1

            # compare gradients dy1 / dx1 and dy2 / dx2
            # but we have to avoid floating-points issues:
            # if   dy1 / dx1 = dy2 / dx2
            # then dy1 * dx2 = dy2 * dx1
            # using Python's big integers
            # but we actually need to check for inequality
            result += (dy1 * dx2 != dy2 * dx1)

            dx1 = dx2
            dy1 = dy2

        return result
